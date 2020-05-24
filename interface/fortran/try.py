import numpy as np
from fortran_module import add

x = np.arange(10.)
y = np.arange(0.1, 10.1)
z = add(x, y)

print(z)
