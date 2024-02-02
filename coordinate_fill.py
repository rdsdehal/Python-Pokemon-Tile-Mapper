import json
from map_grid import *

with open("map16_coordinates.txt", "r") as file:
    # Read the content and parse it as JSON
    no_walk_coords = json.loads(file.read())

# Convert each coordinate from 'x,y' format into a tuple (x, y)
no_walk_coords = [tuple(map(int, coord.split(','))) for coord in no_walk_coords]

# Now we can fill these tiles with white color and show the grid on the map.

# Create a new figure and axis to plot the image
fig, ax = plt.subplots(figsize=(12, 15))

# Display the image
ax.imshow(img)

# Fill each no-walk tile with white color
for coord in no_walk_coords:
    x, y = coord
    rect = patches.Rectangle((x - tile_size, y - tile_size), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='white')
    ax.add_patch(rect)

# Overlay the grid on the image
for x in range(0, image_size[0], tile_size):
    for y in range(0, image_size[1], tile_size):
        rect = patches.Rectangle((x, y), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

# Remove axis labels for clarity
ax.axis('off')

# Show the modified image
plt.show()
