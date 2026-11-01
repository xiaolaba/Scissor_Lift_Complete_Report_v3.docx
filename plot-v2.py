import numpy as np
import matplotlib.pyplot as plt

# 1. 最新條件參數
delta_x_max = 53.0  # 最大水平行程 (mm)
n_max = 25.0        # 最大螺絲轉數 (圈)
pitch = delta_x_max / n_max  # 有效牙距 = 2.12 mm/圈
L = 35.0            # 單臂半長 35 mm，總臂長 70 mm

# 2. 運動學計算
n_vals = np.linspace(0, 25, 200)
X_vals = 70.0 - (n_vals * pitch)
H_vals = np.sqrt(70.0**2 - X_vals**2)

# 3. 繪製運動學變化曲線
plt.figure(figsize=(7, 4.2), dpi=300)
plt.plot(n_vals, H_vals, color='#1B365D', linewidth=2.5, label=r'$h(n) = \sqrt{70^2 - (70 - 2.12n)^2}$')
plt.scatter([0, 5, 10, 15, 20, 25], 
            [0, 36.92, 50.15, 58.62, 64.33, 67.91], 
            color='#D9534F', zorder=5, s=40)

plt.title('Scissor Lift Height vs. Screw Revolutions (Max Stroke 53mm / 25 Turns)', fontsize=11, fontweight='bold')
plt.xlabel('Screw Revolutions n (turns, pitch = 2.12mm)', fontsize=10)
plt.ylabel('Vertical Height h (mm)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, 27)
plt.ylim(0, 75)
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()