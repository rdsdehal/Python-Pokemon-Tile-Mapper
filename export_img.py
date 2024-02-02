import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json

# Function to add labels to the tiles
def label_tile(ax, coord, tile_size):
    x, y = coord
    label = f"{x},{y}"
    ax.text(x, y, label, color='blue', ha='center', va='center', fontsize=6)

# Load the image
img = Image.open("map1.png")

# Size of the image and tiles in pixels
image_size = (840, 1104)  # Width x Height
tile_size = 16

# Read the file with the coordinates
with open("map1_coordinates.txt", "r") as file:
    # Read the content and parse it as JSON
    no_walk_coords = json.loads(file.read())

# Convert string coordinates into tuples of integers
no_walk_coords = [tuple(map(int, coord.split(','))) for coord in no_walk_coords]

# Create a figure and axis to plot the image
fig, ax = plt.subplots(figsize=(12, 15))

# Display the image
ax.imshow(img)

# Fill each no-walk tile with white color and label it
for coord in no_walk_coords:
    x, y = coord
    rect = patches.Rectangle((x - tile_size, y - tile_size), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='white')
    ax.add_patch(rect)
    # label_tile(ax, (x, y), tile_size)  # Uncomment to label tiles

# Overlay the grid on the image
for x in range(0, image_size[0], tile_size):
    for y in range(0, image_size[1], tile_size):
        rect = patches.Rectangle((x, y), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

# Remove axis labels for clarity
ax.axis('off')

# Define the output path
output_path = "map_with_grid.png"

# Save the figure
plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1, dpi=300)

# Return the path to the saved image
print(output_path)
