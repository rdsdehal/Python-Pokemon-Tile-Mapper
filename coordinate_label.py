# Create a new figure and axis to plot the image with labeled coordinates
from map_grid import *

fig, ax = plt.subplots(figsize=(12, 15))

# Display the image
ax.imshow(img)

# Define a function to label the tiles with their coordinates
def label_tile(ax, coord, tile_size):
    x, y = coord
    label = f"{x},{y}"
    ax.text(x - tile_size / 2, y - tile_size / 2, label, color='blue', ha='center', va='center', fontsize=4)

# Fill each no-walk tile with white color and label it
for coord in no_walk_coords:
    x, y = coord
    rect = patches.Rectangle((x - tile_size, y - tile_size), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='white')
    ax.add_patch(rect)
    label_tile(ax, (x, y), tile_size)

# Overlay the grid on the image
for x in range(0, image_size[0], tile_size):
    for y in range(0, image_size[1], tile_size):
        rect = patches.Rectangle((x, y), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

# Remove axis labels for clarity
ax.axis('off')

# Show the modified image
plt.show()
