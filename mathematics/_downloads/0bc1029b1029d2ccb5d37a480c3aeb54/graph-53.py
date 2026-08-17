import matplotlib.pyplot as plt
from solve_751 import solve_bvp  # Nhập hàm từ solver.py

# Giải phương trình và lấy dữ liệu
x, y, z, z0_final = solve_bvp()

# Vẽ đồ thị
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f"y(x) (y'(0) = {z0_final:.2f})", color='blue')
plt.scatter([0, 1], [0, -1], color='red', label="Điều kiện biên", zorder=5)
plt.title("Nghiệm của phương trình $y'' - y = 2x$")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()