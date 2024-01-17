# Adding Points of Interest to the ASCII rogue-like style map

# Define Points of Interest (POIs)
poi_symbols = {
    "S": "Sniper vantage point",
    "B": "Bridge",
    "C": "Crumbled building",
    "O": "Open ground",
    "K": "Catwalks",
    "P": "Central platform",
    "H": "Dilapidated shelter",
    "L": "Lookout post",
    "M": "Abandoned machinery",
    "D": "Broken downpipes",
    "U": "Underground entrance",
    "A": "Alleyway",
    "T": "Toxic sludge pit",
    "R": "Ruined outpost",
    "F": "Foliage",
    "E": "Map edge"
}

# Update the map grid with POIs
ascii_map_with_poi = [
    ["#", "#", "#", "#"],
    ["#", "S", "B", "#"],
    ["C", "O", "K", "P"],
    ["#", "H", "U", "#"],
    ["#", "T", "R", "E"]
]

# Convert updated ASCII map to a NumPy array
map_array_poi = np.array(ascii_map_with_poi)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Plot each cell with the corresponding symbol
for y in range(map_array_poi.shape[0]):
    for x in range(map_array_poi.shape[1]):
        char = map_array_poi[y, x]
        color = colors.get(char, 'white')  # Default to white if not a wall
        rect = plt.Rectangle((x, map_array_poi.shape[0] - y - 1), 1

