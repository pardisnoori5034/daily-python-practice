import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def model_exp(x, A, tau, C):
    return A * np.exp(-x / tau) + C


x = np.linspace(0, 10, 100)


A_real = 5.0
tau_real = 2.0
C_real = 1.0


noise = np.random.normal(0, 0.2, len(x))


y_noisy = model_exp(x, A_real, tau_real, C_real) + noise

initial_guess = [1.0, 1.0, 1.0]


popt, pcov = curve_fit(model_exp, x, y_noisy, p0=initial_guess)


A_fit = popt[0]
tau_fit = popt[1]
C_fit = popt[2]


print("Reasilts")
print(f"real parameters:   A = {A_real}, tau = {tau_real}, C = {C_real}")
print(f"discovered parameters: A = {A_fit:.3f}, tau = {tau_fit:.3f}, C = {C_fit:.3f}")

plt.scatter(x, y_noisy, label='Noisy Data', color='red', s=15, alpha=0.7)


y_fit = model_exp(x, A_fit, tau_fit, C_fit)
plt.plot(x, y_fit, label='Exponential Fit', color='blue', linewidth=2)

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Exponential Fit: $y = A e^{-x/\tau} + C$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


