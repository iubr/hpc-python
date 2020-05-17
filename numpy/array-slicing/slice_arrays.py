import numpy as np

twoD = np.random.rand(4,4)
print(twoD)

print("1. Every element from the second row: ")
print(twoD[1,:])

print("2. Ever element from the third column: ")
print(twoD[:,2])

twoD[:2,:2] = 0.21
print(twoD)


checker = np.zeros((8,8))
print(checker)

checker[::2,::2] = 1
#checker[1::2,1::2] = 1
##for i in range(checker.shape[0]):
##	for j in range(i, checker.shape[1]):
##		if i % 2 == 0 and j % 2 == 0:
##			checker[i,j] = 1
##			checker[j,i] = 1
##		elif i % 2 != 0 and j % 2 !=0:
##			checker[i,j] = 1
##			checker[j,i] = 1

print("New: ")
print(checker)
