#%%
import matplotlib.pyplot as plt
import numpy as np

# Creating a top-down, simplified graphical representation of the map

# Define the map grid with colors and shapes for different features
graphical_map = {
    (0, 0): ("black", "square"),  # Wall
    (0, 1): ("black", "square"),  # Wall
    (0, 2): ("black", "square"),  # Wall
    (0, 3): ("black", "square"),  # Wall
    (1, 0): ("black", "square"),  # Wall
    (1, 1): ("green", "circle"),  # Shelter
    (1, 2): ("purple", "circle"), # Toxic area
    (1, 3): ("black", "square"),  # Wall
    (2, 0): ("white", "circle"),  # Open space
    (2, 1): ("white", "circle"),  # Open space
    (2, 2): ("white", "circle"),  # Open space
    (2, 3): ("white", "circle"),  # Open space
    (3, 0): ("black", "square"),  # Wall
    (3, 1): ("blue", "circle"),   # High ground
    (3, 2): ("orange", "circle"), # Cover
    (3, 3): ("black", "square"),  # Wall
    (4, 0): ("black", "square"),  # Wall
    (4, 1): ("black", "square"),  # Wall
    (4, 2): ("black", "square"),  # Wall
    (4, 3): ("black", "square"),  # Wall
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot each cell with the corresponding color and shape
for position, (color, shape) in graphical_map.items():
    if shape == "circle":
        circle = plt.Circle((position[1] + 0.5, 5 - position[0] - 0.5), 0.4, color=color)
        ax.add_patch(circle)
    elif shape == "square":
        square = plt.Rectangle((position[1], 5 - position[0] - 1), 1, 1, color=color)
        ax.add_patch(square)

# Set up the plot with grid coordinates
ax.set_xlim(0, 4)
ax.set_ylim(0, 5)
ax.set_xticks(np.arange(0, 4, 1))
ax.set_yticks(np.arange(0, 5, 1))
ax.set_xticklabels(['A', 'B', 'C', 'D'])
ax.set_yticklabels(['5', '4', '3', '2', '1'])
ax.grid(which='both', color='grey', linestyle='-', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')

# Add a legend for colors
colors_legend = {'black': 'Wall', 'green': 'Shelter', 'purple': 'Toxic area', 'blue': 'High ground', 'orange': 'Cover', 'white': 'Open space'}
text_legend = "\n".join([f"{color}: {meaning}" for color, meaning in colors_legend.items()])
fig.text(0.75, 0.5, "Legend:\n" + text_legend, fontsize=12, va='center')

# Show the plot
plt.show()
