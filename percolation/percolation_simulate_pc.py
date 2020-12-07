import numpy.random as rn
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements as mm
import random as rnd

def check_if_matches(a1, a2, n):
    a = [0 for i in range(n+1)]
    for i in a1:
        a[i] = 1
    for i in a2:
        if i != 0 and a[i] == 1:
            return True
    return False

def binary_search(func, l, r, depth, max_depth):
    p = (l+r)/2
    if depth == max_depth:
        return p
    if func(p):
        return binary_search(func, l, p, depth+1, max_depth)
    else:
        return binary_search(func, p, r, depth+1, max_depth)

def create_data(L, p, loop):
    for i in range(loop):
        rng = rn.RandomState(int(rnd.random()*100))
        d = rng.rand(L, L)
        m = d < p
        lw, num = mm.label(m)
        a1, a2 = lw[0], lw[-1]

        if not check_if_matches(a1, a2, num):
            return False
    return True

def simulate(L):
    l, r = 0, 1
    L = int(L//3)
    depth = int(np.log2(L))
    loop = L
    def func(p):
        return create_data(L, p, loop)
    
    answer = binary_search(func, l, r, 0, depth)
    print(answer)
    return answer


x = np.linspace(4, 1000, 20)
y = [simulate(i) for i in x]

plt.plot(x, y)
plt.show()


# rng=rn.RandomState(10)
# data=rn.rand(L, L)
# m = data < p
# lw, num = mm.label(m)

# plt.imshow(m, origin='lower')
# plt.show()

# sorted colors
# area = mm.sum(m, lw, index=np.arange(lw.max()+1))
# al = area[lw]

# plt.imshow(al, origin='lower', cmap='Greys')
# plt.show()

# lw, num = mm.label(m)




# # shuffled colors
# b = np.arange(lw.max()+1)
# shuffle(b[1:])
# l = b[lw]

