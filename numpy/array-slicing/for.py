#import numpy as np
import timeit

import_module = "import numpy as np"
testfor = '''
N = 1000
arr = np.arange(N)
diff = np.zeros(N-1)

for i in range(N):
	diff[i-1] = arr[i] - arr[i-1]
'''

testslice = '''
N = 1000
arr = np.arange(N)
diff = np.zeros(N-1)

diff = arr[1:] - arr[:-1]
'''

print("For: ", timeit.timeit(stmt=testfor, setup=import_module))
print("Slice: ", timeit.timeit(stmt=testslice, setup=import_module)) 
