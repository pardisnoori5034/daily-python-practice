import numpy as np
import matplotlib.pyplot as plt


epsilon_0 = 8.854e-12  
k_B = 1.38e-23       
e = 1.602e-19       
T_e = 10000           

n_e = np.logspace(16, 22, 100) 


lambda_D = np.sqrt((epsilon_0 * k_B * T_e) / (n_e * e**2))


plt.figure(figsize=(8, 5))
plt.plot(n_e, lambda_D, color='blue', linewidth=2)


plt.xscale("log")  
plt.yscale("log")

 
plt.xlabel("Electron Density ($n_e$) [m^-3]")
plt.ylabel("Debye Length ($\lambda_D$) [m]")
plt.title("Debye Length vs Electron Density")
plt.grid(True, which="both", ls="-", alpha=0.5)

plt.show()
