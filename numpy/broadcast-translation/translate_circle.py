import numpy as np
import matplotlib.pyplot as plt

inp = open("points_circle.dat", "r")
num_lines = sum(1 for line in open('points_circle.dat'))

original = np.zeros((num_lines, 2))
for i in range(num_lines):
	line = inp.readline()
	parts = line.split()
	original[i,0] =  float(parts[0])
	original[i,1] = float(parts[1])

print(original[:,0])
plt.plot(original[:,0], original[:,1], 'o')
plt.plot(original[:,0]+2.1, original[:,1]+1.1, 'x')
plt.show()
