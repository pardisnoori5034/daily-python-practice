import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x=np.linspace(0,10,40)
a_real = 2.5
b_real = 1.2
noise = np.random.normal(0,0.8,len(x))

y_noisy = a_real * x + b_real + noise 

def model_func(x,a,b):
    return a*x +b

popt,pcov = curve_fit(model_func,x,y_noisy)

a_fit = popt[0]
b_fit = popt[1]
 
print(f" y = {a_real}x + {b_real}")
print(f"y = {a_fit:.2f}x + {b_fit:.2f}")


plt.scatter(x,y_noisy,label='Data With Noise',color='red',s=20)
plt.plot(x,model_func(x,a_fit,b_fit),label='fitted line', color='blue', linewidth=2)

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Fit using Scipy')
plt.show()