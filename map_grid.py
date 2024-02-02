import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# Load the image
img = Image.open("map16.png")

# Create a figure and axis to plot the image
fig, ax = plt.subplots(figsize=(12, 15))

# Display the image
ax.imshow(img)

# Size of the image and tiles in pixels
image_size = (840, 1104)
tile_size = 16

# Number of tiles along the x and y axis
x_tiles = image_size[0] // tile_size
y_tiles = image_size[1] // tile_size

# Create a grid over the image
for x in range(0, image_size[0], tile_size):
    for y in range(0, image_size[1], tile_size):
        rect = patches.Rectangle((x, y), tile_size, tile_size, linewidth=0.5, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

# Remove axis labels for clarity
ax.axis('off')

plt.show()
