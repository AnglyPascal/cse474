import sympy
from sympy import *

init_printing(use_unicode=True)
x, y, z = symbols('x y z')

# expr= x + x*y + x**3
# pprint(factor(expr))

# e2 = sin(x)**2 + (cos(x)+1)**2
# print(simplify(e2))
# pprint(expand((x-y)*(x+y)))

# d = simplify(diff(x**2 + x**3 + x**10, x, 3))
d = pi*x**2 + x*2 + 1
pprint(d.subs(x, 2))
