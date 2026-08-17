import math

def f(x, y):
    return (-2 * x * y**2) / (x**2 - 1)

def rk4_step(f, x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x_next = x + h
    return x_next, y_next

def solve_ode(f, x0, y0, h, x_end):
    x = x0
    y = y0
    solution = [(x, y)]
    while x < x_end:
        if x + h > x_end:
            h = x_end - x
        x, y = rk4_step(f, x, y, h)
        solution.append((x, y))
    return solution

def analytical_solution(x):
    if x < 1:
        denominator = 1 + math.log(1 - x**2)
        if denominator != 0:
            return 1 / denominator
    return float('inf')

# Tham số
x0 = 0.0
y0 = 1.0
x_end = 0.7  # Giải đến x = 0.7 để tránh điểm kỳ dị
h_values = [0.1, 0.05, 0.025, 0.0125, 0.00625]  # 5 giá trị h giảm dần

# Giải và so sánh cho từng h
for h in h_values:
    print(f"\n{'='*50}")
    print(f"Kết quả với h = {h:.5f}")
    print(f"{'='*50}")
    
    # Giải bằng RK4
    solution = solve_ode(f, x0, y0, h, x_end)
    
    # In header
    print(f"{'x':<10}{'y_RK4':<20}{'y_analytical':<20}{'Sai số':<20}")
    print(f"{'-'*60}")
    
    # Tính và in kết quả
    for point in solution:
        x = point[0]
        y_rk4 = point[1]
        y_analytical = analytical_solution(x)
        
        # Tính sai số (tránh trường hợp nghiệm giải tích là vô cùng)
        if math.isfinite(y_analytical):
            error = abs(y_rk4 - y_analytical)
        else:
            error = float('inf')
        
        print(f"{x:<10.5f}{y_rk4:<20.10f}{y_analytical:<20.10f}{error:<20.10f}")