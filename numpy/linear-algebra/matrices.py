import numpy as np

aA = np.random.rand(4,4)
aB = np.random.rand(4,4)
A = aA+aA.transpose()
B = aB+aB.transpose()
print(A)
print()
print(B)
print()

C = np.dot(A,B)
print(C)
print()
w = np.linalg.eigvals(C)
print("The eigenvalues are: ", w)
