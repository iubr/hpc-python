import numpy as np
from math import pi
import matplotlib.pyplot as plt

a = 0.0
b = 0.5*pi
steps = np.arange(0.01, 1.0, 0.01)
ints = np.zeros(steps.shape)

i = 0
for dx in steps:
	x = np.arange(a, b, dx)
	xp = 0.5*(x[:-1]+x[1:])
	fxp = np.sin(xp)
	S = np.sum(fxp*dx)

	print("With dx: ", dx, ", the integral is: ", S)

	ints[i] = S
	i += 1

plt.plot(steps, ints)
plt.show()
