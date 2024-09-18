import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1000)
y = np.sin(x)

plt.plot(x,y)

plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.title('Graphique de la fonction sinusoidale')

plt.grid(True)
plt.savefig('sinus.png', dpi=300)