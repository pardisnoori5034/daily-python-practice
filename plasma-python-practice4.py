import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,np.pi*2,100)
y = np.sin(x)

noise = np.random.normal(0,0.2,len(x))

y_noisy = y + noise

plt.plot(x,y,label="clean")
plt.scatter(x,y_noisy,color='red',label="Noisy")

window = 5
kernal = np.ones(window)/window
y_smooth = np.convolve(y_noisy,kernal,mode='valid')
x_smooth = x[window-1:]

plt.plot(x_smooth,y_smooth,label="smoothed",color='green',linewidth=3)
plt.legend()
plt.show()
