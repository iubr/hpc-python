import numpy as np

arr = np.random.rand(2,4)
print(arr)
print("Original array, " , arr.shape)
print()
spl = np.split(arr, 2, axis=1)
a = spl[0]
b = spl[1]
print(a)
print()
print(b)
print()
new = np.concatenate((a,b))
print(new)
