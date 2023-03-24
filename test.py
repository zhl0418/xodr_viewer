import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametric equations for a 3D spiral
def spiral(t, a, b):
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    return x, y, z

# Parameters for the spiral
a = 1
b = 0.2
t = np.linspace(0, 10 * np.pi, 1000)  # t values from 0 to 10 * pi

# Calculate the x, y, and z coordinates
x, y, z = spiral(t, a, b)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, label='3D Spiral')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

plt.show()
