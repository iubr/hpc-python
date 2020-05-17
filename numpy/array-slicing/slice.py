import numpy as np

N = 1000
arr = np.arange(N)
diff = np.zeros(N-1)

diff = arr[1:] - arr[:-1]
