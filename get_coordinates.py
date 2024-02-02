from PIL import Image
import numpy as np

# Load the image
img = Image.open("map_with_grid_white.png")
pixels = np.array(img)

# The size of each tile in pixels
tile_size = 16

# Calculate the size of the grid
grid_size_x = pixels.shape[1] // tile_size
grid_size_y = pixels.shape[0] // tile_size

# List to hold the coordinates of white tiles
white_tile_coords = []

# Iterate over the grid
for y in range(0, grid_size_y):
    for x in range(0, grid_size_x):
        # Calculate the pixel coordinates of the top-left corner of the tile
        pixel_x = x * tile_size
        pixel_y = y * tile_size

        # Get the tile from the image
        tile = pixels[pixel_y:pixel_y + tile_size, pixel_x:pixel_x + tile_size]

        # Check if the majority of the pixels in the tile are white
        if np.mean(tile >= 240) > 0.5:  # More than half of the pixels are white
            # The tile is considered white, add its coordinates to the list
            white_tile_coords.append((pixel_x, pixel_y))

# Output the list of white tile coordinates
print(white_tile_coords)
