
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource

# Enhancing the 3D map for better readability

# Define a more pronounced elevation map with clear terrain types
enhanced_elevation_map = np.array([
    [4, 1, 1, 4],  # Wall, Shelter, Toxic area, Wall
    [0, 0, 0, 0],  # Open space
    [4, 3, 2, 4],  # Wall, High ground, Cover, Wall
])

# Use a more distinct color map
ls = LightSource(270, 45)
rgb_enhanced = ls.shade(enhanced_elevation_map, cmap=cm.terrain, vert_exag=0.5, blend_mode='soft')

# Set up a 3D plot with enhanced features
fig, ax = plt.subplots(subplot_kw={'projection': '3d'}, figsize=(8, 6))

# Plot the enhanced surface
surf = ax.plot_surface(x, y, enhanced_elevation_map, rstride=1, cstride=1, facecolors=rgb_enhanced,
                       linewidth=0, antialiased=False, shade=False)

# Adjust viewing angle for better perspective
ax.view_init(elev=45, azim=-60)

# Add labels for key areas
key_areas = {
    (0, 1): "Shelter",
    (0, 2): "Toxic Area",
    (2, 1): "High Ground",
    (2, 2): "Cover"
}

for (y, x), label in key_areas.items():
    ax.text(x, y, enhanced_elevation_map[y, x] + 0.5, label, color='white', ha='center', va='center')

# Set axis labels and title
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Elevation')
ax.set_title('Enhanced Necromunda Map with Elevation')

# Show the enhanced plot
plt.show()