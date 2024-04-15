import numpy as np
import matplotlib.pyplot as plt
#Matplotlib tiene muchos modulos, para importar un solo modulo es matplotlib.modulo 

#Crear ndarray de 1 sola dimencion, 100 elementos equiespaciados, de 0 a 2*pi

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

#usar matplotlib

plt.figure(figsize=(8,4))

plt.plot(x,y)
plt.show()