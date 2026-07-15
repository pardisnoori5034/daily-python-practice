import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

x=np.linspace(0,np.pi,200)
y=np.sin(x)
y1=np.trapz(y,x)

def f(x):
    return np.sin(x)

y2,error = quad(f,0,np.pi)

print("y1(trapz):",y1)
print("y2(quad):",y2)