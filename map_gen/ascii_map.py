#%%
import matplotlib.pyplot as plt
import numpy as np


# Creating a rogue-like ASCII style map using Matplotlib

# Define the map grid with ASCII-style symbols
ascii_map = [
    ["#", "#", "#", "#"],
    ["#", ".", ".", "#"],
    [".", ".", ".", "."],
    ["#", ".", ".", "#"],
    ["#", "#", "#", "#"]
]

# Convert ASCII map to a NumPy array for easy handling
map_array = np.array(ascii_map)

# Create a color map: empty space (.), wall (#)
colors = {'#': 'black', '.': 'white'}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Plot each cell with the corresponding color
for y in range(map_array.shape[0]):
    for x in range(map_array.shape[1]):
        char = map_array[y, x]
        rect = plt.Rectangle((x, map_array.shape[0] - y - 1), 1, 1, color=colors[char])
        ax.add_patch(rect)

# Set up the plot
ax.set_xlim(0, map_array.shape[1])
ax.set_ylim(0, map_array.shape[0])
ax.set_xticks(np.arange(0, map_array.shape[1], 1))
ax.set_yticks(np.arange(0, map_array.shape[0], 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_aspect('equal', adjustable='box')
ax.axis('off')  # Turn off the axis for a clean, game-like appearance

# Show the plot
plt.show()
# %%
