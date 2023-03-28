import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the two lines as lists of points (x, y, z)
line1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
line2 = np.array([[0, 0, 3], [1, 1, 4], [2, 2, 5], [3, 3, 6]])

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the lines
ax.plot(line1[:, 0], line1[:, 1], line1[:, 2], 'r', label='Line 1')
ax.plot(line2[:, 0], line2[:, 1], line2[:, 2], 'b', label='Line 2')

# Create the surface between the lines
for i in range(len(line1) - 1):
    x = np.array([[line1[i, 0], line1[i+1, 0]], [line2[i, 0], line2[i+1, 0]]])
    y = np.array([[line1[i, 1], line1[i+1, 1]], [line2[i, 1], line2[i+1, 1]]])
    z = np.array([[line1[i, 2], line1[i+1, 2]], [line2[i, 2], line2[i+1, 2]]])
    ax.plot_surface(x, y, z, alpha=0.5, color='g')

# Set labels and show the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()

