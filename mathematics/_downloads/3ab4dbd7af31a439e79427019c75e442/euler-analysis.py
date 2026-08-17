import numpy as np
import matplotlib.pyplot as plt
import math

def f_euler(x, y):
    return (-2 * x * y**2) / (x**2 - 1)

def f_solution(x):
    return 1 / (math.log(abs(x**2-1)) + 1)  
x0 = 0.0
y0 = 1.0
x_max = 0.999999999999
num_h = 10 
n = 10      


h_list = [x_max / (10 * (2 ** k)) for k in range(num_h)]
epsilon_list = []


all_x_values = []
all_y_values = []
all_y_solution = []

for h in h_list:
    
    x_values = np.zeros(n + 1)
    y_values = np.zeros(n + 1)
    y_solution = np.zeros(n + 1)
    delta_y = np.zeros(n + 1)

    
    x_values[0] = x0
    y_values[0] = y0
    y_solution[0] = f_solution(x0)
    delta_y[0] = abs(y_solution[0] - y_values[0])

    for i in range(n):
        x = x_values[i]
        y = y_values[i]

        
        if x >= x_max:
            break

        
        x_next = x + h
        if x_next > x_max:
            x_next = x_max

        y_next = y + h * f_euler(x, y)
        y_true_next = f_solution(x_next)

       
        x_values[i + 1] = x_next
        y_values[i + 1] = y_next
        y_solution[i + 1] = y_true_next
        delta_y[i + 1] = abs(y_true_next - y_next)

    
    max_error = np.max(delta_y)
    epsilon_list.append(max_error)

    
    all_x_values.append(x_values)
    all_y_values.append(y_values)
    all_y_solution.append(y_solution)
    
    
    print(f"\n=== for h = {h:.12f} ===")
    print(f"Max error (epsilon): {max_error:.12f}")
    print("x".ljust(15), "y_euler".ljust(15), "y_exact".ljust(15), "error")
    for x, y, yt, err in zip(x_values, y_values, y_solution, delta_y):
        print(f"{x:.10f}".ljust(15), 
              f"{y:.10f}".ljust(15),
              f"{yt:.10f}".ljust(15),
              f"{err:.5f}")


print("\n=== epsilon and h ===")
print("h".ljust(20), "epsilon".ljust(20))
for h, epsilon in zip(h_list, epsilon_list):
    print(f"{h:.12f}".ljust(20), f"{epsilon:.12f}".ljust(20))


ln_h_list = [math.log(h) for h in h_list]
ln_epsilon_list = [math.log(epsilon) for epsilon in epsilon_list]

print("\n===  ln(h) and ln(epsilon) ===")
print("ln(h)".ljust(20), "ln(epsilon)".ljust(20), "alpha".ljust(20))
for ln_h, ln_epsilon in zip(ln_h_list, ln_epsilon_list):
    alpha = ln_epsilon / ln_h if ln_h != 0 else float('inf')  
    print(f"{ln_h:.12f}".ljust(20), f"{ln_epsilon:.12f}".ljust(20), f"{alpha:.12f}".ljust(20))
    



# =============================================
# 1. Vẽ đồ thị so sánh nghiệm Euler và nghiệm chính xác
# =============================================
plt.figure(figsize=(12, 8))

# Chọn 3 giá trị h tiêu biểu để so sánh
selected_indices = [0, 4, 9]  # h lớn nhất, trung bình và nhỏ nhất
colors = ['red', 'green', 'blue']
labels = [f'h = {h_list[i]:.2e}' for i in selected_indices]

# Vẽ nghiệm chính xác
x_dense = np.linspace(x0, x_max, 1000)
y_dense = [f_solution(x) for x in x_dense]
plt.plot(x_dense, y_dense, 'k-', linewidth=3, label='Nghiệm chính xác')

# Vẽ nghiệm Euler cho các h được chọn
for idx, color, label in zip(selected_indices, colors, labels):
    x_vals = all_x_values[idx]
    y_vals = all_y_values[idx]
    # Lọc các điểm hợp lệ
    mask = (x_vals <= x_max) & (x_vals >= x0)
    plt.plot(x_vals[mask], y_vals[mask], 'o--', color=color, markersize=6, label=label)

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('SO SÁNH NGHIỆM EULER VÀ NGHIỆM CHÍNH XÁC', fontsize=14)
plt.legend()
plt.grid(True)
plt.xlim(x0, x_max)
plt.ylim(0, 1.1)

# =============================================
# 2. Vẽ đồ thị tốc độ hội tụ của phương pháp
# =============================================
plt.figure(figsize=(12, 6))

# Tính ln(h) và ln(epsilon)
ln_h_list = [math.log(h) for h in h_list]
ln_epsilon_list = [math.log(epsilon) for epsilon in epsilon_list]

# Vẽ đường dữ liệu
plt.plot(ln_h_list, ln_epsilon_list, 'bo-', linewidth=2, markersize=8, label='Dữ liệu thực tế')

# Vẽ đường hồi quy tuyến tính
slope, intercept = np.polyfit(ln_h_list, ln_epsilon_list, 1)
regression_line = [slope * x + intercept for x in ln_h_list]
plt.plot(ln_h_list, regression_line, 'r--', linewidth=2, label=f'Đường hồi quy (độ dốc = {slope:.4f})')

plt.xlabel('ln(h)', fontsize=12)
plt.ylabel('ln(ε)', fontsize=12)
plt.title('TỐC ĐỘ HỘI TỤ CỦA PHƯƠNG PHÁP EULER', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.figure(figsize=(15, 5))


plt.subplot(1, 2, 1)
plt.loglog(h_list, epsilon_list, 'ro-', markersize=8)
plt.xlabel('Step size h (log scale)')
plt.ylabel('Maximum error (epsilon) (log scale)')
plt.title(' h and epsilon')
plt.grid(True, which='both', linestyle='--')


plt.subplot(1, 2, 2)
plt.plot(ln_h_list, ln_epsilon_list, 'bo-', markersize=8)
plt.xlabel('ln(h)')
plt.ylabel('ln(epsilon)')
plt.title(' ln(h) and ln(epsilon)')
plt.grid()

plt.tight_layout()
plt.show()
