import numpy as np
import matplotlib.pyplot as plt

normal = np.random.normal(loc=4.56, scale=5.0, size=10000)
print(normal)

print("Mean:", np.mean(normal), "Std:", np.std(normal))
plt.hist(normal)
plt.show()
