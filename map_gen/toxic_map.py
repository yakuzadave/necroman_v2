#%%
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Define the map size and cell details
map_size = (4, 4)
cells = {
    (0, 0): "A1\nHigh rooftop",
    (0, 1): "A2\nNarrow bridge",
    (0, 2): "A3\nCrumbled building",
    (0, 3): "A4\nOpen ground",
    (1, 0): "B1\nCatwalks",
    (1, 1): "B2\nCentral platform",
    (1, 2): "B3\nDilapidated shelter",
    (1, 3): "B4\nLookout post",
    (2, 0): "C1\nAbandoned machinery",
    (2, 1): "C2\nBroken downpipes",
    (2, 2): "C3\nUnderground entrance",
    (2, 3): "C4\nBarricaded alleyway",
    (3, 0): "D1\nToxic sludge pit",
    (3, 1): "D2\nRuined outpost",
    (3, 2): "D3\nOvergrown foliage",
    (3, 3): "D4\nMap edge"
}

# Draw the grid and label cells
for (i, j), label in cells.items():
    ax.text(j + 0.5, map_size[0] - i - 0.5, label, ha='center', va='center', fontsize=8)
    rect = plt.Rectangle((j, map_size[0] - i - 1), 1, 1, fill=None, edgecolor='black', lw=1)
    ax.add_patch(rect)

# Set up the plot
ax.set_xlim(0, map_size[1])
ax.set_ylim(0, map_size[0])
ax.set_xticks(np.arange(0, map_size[1], 1))
ax.set_yticks(np.arange(0, map_size[0], 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
# %%
