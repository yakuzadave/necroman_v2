"""
Adjusting the voxel data to be 3-dimensional for the Necromunda scenario.
"""

import matplotlib.pyplot as plt
import numpy as np

# Redefine the voxel array with an additional dimension for height
voxel_array_3d = np.zeros((3, 4, 4), dtype=bool)

# Define walls
voxel_array_3d[:, 0, 0] = True
voxel_array_3d[:, 0, 3] = True
voxel_array_3d[:, 2, 0] = True
voxel_array_3d[:, 2, 3] = True

# Define special features at ground level
voxel_array_3d[0, 1, 1] = True  # Shelter
voxel_array_3d[0, 1, 2] = True  # Toxic area

# Define colors for each voxel
colors_3d = np.empty(voxel_array_3d.shape, dtype=object)
colors_3d[voxel_array_3d] = 'grey'  # Default color for walls

# Assign colors to special features
colors_3d[0, 1, 1] = 'green'  # Shelter
colors_3d[0, 1, 2] = 'purple' # Toxic area

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the voxels
ax.voxels(voxel_array_3d, facecolors=colors_3d, edgecolor='k')

# Set plot labels and title
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z (Height)')
ax.set_title('Necromunda 3D Voxel Map')

# Show the plot
plt.show()
