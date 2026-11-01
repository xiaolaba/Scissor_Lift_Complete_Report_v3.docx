import numpy as np
import matplotlib.pyplot as plt

# 1. 機構參數
delta_x_max = 53.0  # 最大水平行程 (mm)
n_max = 25.0        # 最大螺絲轉數 (圈)
pitch = delta_x_max / n_max  # 有效導程牙距 = 2.12 mm/圈
L = 35.0            # 單臂半長 35 mm，總臂長 70 mm

# 2. 運動學計算 (n: 0 -> 25)
n_vals = np.linspace(0, 25, 200)
X_vals = 70.0 - (n_vals * pitch)       # 水平跨度 X(n)
Y_vals = np.sqrt(70.0**2 - X_vals**2)  # 垂直高度 Y(n)

# 3.1 繪製 螺絲轉數 vs 垂直高度 曲線圖 (n vs h)
plt.figure(figsize=(7, 4.2), dpi=300)
plt.plot(n_vals, Y_vals, color='#1B365D', linewidth=2.5, label=r'$h(n) = \sqrt{70^2 - (70 - 2.12n)^2}$')
plt.scatter([0, 5, 10, 15, 20, 25], [0, 37.04, 50.19, 58.66, 64.33, 67.90], color='#D9534F', zorder=5, s=40)
plt.title('Scissor Lift Height vs. Screw Revolutions', fontsize=11, fontweight='bold')
plt.xlabel('Screw Revolutions n (turns, pitch = 2.12mm)', fontsize=10)
plt.ylabel('Vertical Height h (mm)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, 27)
plt.ylim(0, 75)
plt.legend(loc='lower right')
plt.tight_layout()

plt.show()

# 3.2 繪製 水平跨度 vs 垂直高度 軌跡圖 (X vs Y)
plt.figure(figsize=(7, 4.2), dpi=300)
plt.plot(X_vals, Y_vals, color='#1B365D', linewidth=2.5, label=r'$Y(X) = \sqrt{70^2 - X^2}$')
n_pts = np.array([0, 5, 10, 15, 20, 25])
x_pts = 70.0 - (n_pts * pitch)
y_pts = np.sqrt(70.0**2 - x_pts**2)
plt.scatter(x_pts, y_pts, color='#D9534F', zorder=5, s=40)
for n, x, y in zip(n_pts, x_pts, y_pts):
    plt.annotate(f'{n}圈\n({x:.1f}, {y:.1f})', (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

plt.title('Scissor Lift Trajectory: Horizontal Span (X) vs. Vertical Height (Y)', fontsize=11, fontweight='bold')
plt.xlabel('Horizontal Span X (mm) [70mm → 17mm]', fontsize=10)
plt.ylabel('Vertical Height Y / h (mm)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().invert_xaxis()
plt.xlim(75, 10)
plt.ylim(0, 75)
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()
