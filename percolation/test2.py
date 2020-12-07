from numpy.random import rand
import matplotlib.pyplot as plt
from scipy.ndimage import measurements
import numpy as np
from random import shuffle

p = 0.5
l = rand(5, 5)
m = l < p
lw, num = measurements.label(m)
print(m)
print(lw)

b = np.arange(lw.max() + 1)
shuffle(b[1:])
shuffledLw = b[lw]
print(b)

plt.imshow(shuffledLw, cmap="binary")
plt.savefig('cluster.png', bbox_inches='tight')
# plt.show()
