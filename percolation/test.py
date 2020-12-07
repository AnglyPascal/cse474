import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements

size = 5
data = np.random.rand(size, size)
for i in range(size):
    for j in range(size):
        data[i][j] = round(data[i][j], 2)

# Limits for the extent
x_start = 3.0
x_end = 9.0
y_start = 6.0
y_end = 12.0

extent = [x_start, x_end, y_start, y_end]

# The normal figure
fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
im = ax.imshow(data, extent=extent, origin='lower', interpolation='None', cmap='binary')

# Add the text
jump_x = (x_end - x_start) / (2.0 * size)
jump_y = (y_end - y_start) / (2.0 * size)
x_positions = np.linspace(start=x_start, stop=x_end, num=size, endpoint=False)
y_positions = np.linspace(start=y_start, stop=y_end, num=size, endpoint=False)

for y_index, y in enumerate(y_positions):
    for x_index, x in enumerate(x_positions):
        label = data[y_index, x_index]
        text_x = x + jump_x
        text_y = y + jump_y
        ax.text(text_x, text_y, label, color='black', ha='center', va='center')

# fig.colorbar(im)
plt.savefig('random_array.png', bbox_inches='tight',)
plt.show()

p = 0.5
m = data < p
plt.imshow(m, cmap='binary')
plt.savefig('random_array_true-false.png', bbox_inches='tight')
plt.show()
