import numpy as np
import matplotlib.pyplot as plt

# 1. تعریف بازه x
x = np.linspace(-3, 3, 100)

# 2. تعریف تابع phi
phi = np.exp(-x**2)

# 3. محاسبه مشتق عددی (میدان الکتریکی)
# dphi_dx مشتق phi نسبت به x است
dphi_dx = np.gradient(phi, x)
# میدان الکتریکی منفی مشتق است
E = -dphi_dx

# 4. رسم نمودار
plt.figure(figsize=(10, 6))

plt.plot(x, phi, label='$\phi(x) = e^{-x^2}$', color='blue', linewidth=2)
plt.plot(x, E, label='$E(x) = -d\phi/dx$', color='red', linestyle='--', linewidth=2)

# اضافه کردن جزئیات طبق صورت مسئله
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Potential and Electric Field')
plt.axhline(0, color='black', linewidth=0.5) # خط افقی برای محور صفر
plt.axvline(0, color='black', linewidth=0.5) # خط عمودی برای محور صفر
plt.legend()
plt.grid(True)

# نمایش نمودار
plt.show()