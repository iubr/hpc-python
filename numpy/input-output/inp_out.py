import numpy as np
import matplotlib.pyplot as plt

xy = np.loadtxt("xy-coordinates.dat")
plt.plot(xy[:,0], xy[:,1],'o')

xy[:,1]=xy[:,1]+2.5
plt.plot(xy[:,0], xy[:,1],'x')
plt.show()

args = {
	'header' : 'XY, Y+2.5',
	'fmt': '%10.5f',
	'delimiter': ' ; ', 
}

np.savetxt("output_xy.dat", xy, **args)
