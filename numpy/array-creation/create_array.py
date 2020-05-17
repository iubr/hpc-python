import numpy as np

pylist = (1, 5, 6.71, 4.34, 2.21)
np_array = np.array(pylist)
print(np_array[2])

arr2 = np.arange(-2.0, 2.2, 0.2)
print(arr2)

arr3 = np.linspace(0.5, 1.5, 11)
print(arr3)

py_string = 'AACGTTTTGGGaaaattttaaattgtgcc'

arr4 = np.array(py_string, dtype='c')

print(arr4)
