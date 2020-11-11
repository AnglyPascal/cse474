import numpy as np
from pint import UnitRegistry
ureg = UnitRegistry()
import matplotlib.pyplot as plt


# defining the units
m = ureg.meter
s = ureg.second
kg = ureg.kilogram

height = 150 * m
v_init = 0 * m / s
mass = 1e-3 * kg
diameter = 5e-5 * m
dt = .1 * s

class system:

    def __init__(self, height, v_0, mass, diam, rho, v_t):
        self.height = height
        self.v_0 = v_0
        self.g = 9.8 * m / s**2
        self.acc = 0 * m / s**2
        self.v = v_0
        self.mass = mass
        self.diam = diam
        self.rho = rho
        self.v_t = v_t

        self.area = np.pi * (self.diam/2)**2
        self.C_d = 2 * mass * self.g / (rho * self.area * v_t**2)
        self.state = (self.height, self.v)
        self.T = 30 * s

    def update(self, dt):
        a_drag = self.rho * self.v**2 * self.C_d * self.area / (2 * self.mass)
        self.acc = -self.g + a_drag

        self.height += self.v * dt + self.acc * dt**2 / 2
        self.v += self.acc * dt

        return self.height

sys = system(height, v_init, mass, diameter, 1.2 *kg/m**3, 18 *m/s)

x = [0]
y = [sys.height.magnitude]

while sys.height>0:
    x.append((x[-1] * s + dt).magnitude)
    y.append(sys.update(dt).magnitude)
    print(sys.v.magnitude)

plt.plot(x, y)
plt.show()
