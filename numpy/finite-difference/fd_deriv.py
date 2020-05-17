import numpy as np
from math import pi

dx = 0.1
ang = np.arange(0, 0.5*pi, dx)
sin = np.sin(ang)
cos = np.cos(ang[1:-1])
dsin = np.zeros(sin.shape)
#print(dsin.shape)
dsin = (sin[2:]-sin[:-2])/0.2
print("Sin:", sin.shape, sin)
print("Dsin:",dsin.shape, dsin)
print("Cos:", cos.shape, cos)
