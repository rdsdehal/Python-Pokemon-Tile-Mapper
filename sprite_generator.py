from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import cv2
import random

def generate_star(draw, x, y, radius=3, color=(255, 255, 255, 255)):
    """Draws a basic sparkle star using cross lines"""
    draw.line((x - radius, y, x + radius, y), fill=color)
    draw.line((x, y - radius, x, y + radius), fill=color)
    # Optional: add diagonals for more flair
    draw.line((x - radius, y - radius, x + radius, y + radius), fill=color)
    draw.line((x - radius, y + radius, x + radius, y - radius), fill=color)

def add_glow_and_sparkles(input_path, output_path,
                          glow_color=(255, 200, 255), blur_radius=8,
                          sparkle_count=20, sparkle_color=(255, 255, 255, 180)):
    # Load sprite
    img = Image.open(input_path).convert("RGBA")
    sprite_np = np.array(img)
    alpha = sprite_np[:, :, 3]

    # Create glow from single alpha channel
    glow = cv2.GaussianBlur(alpha, (0, 0), blur_radius)

    # Prepare empty RGBA glow image
    glow_colored = np.zeros_like(sprite_np)

    # Apply color tint to each RGB channel
    for i in range(3):
        glow_colored[:, :, i] = glow * (glow_color[i] / 255.0)

    # Set alpha channel
    glow_colored[:, :, 3] = np.clip(glow, 0, 255)

    # Create glow and sparkle canvas
    glow_img = Image.fromarray(glow_colored.astype(np.uint8), 'RGBA')
    sparkle_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(sparkle_layer)

    # Generate sparkles randomly near the sprite
    h, w = img.size
    for _ in range(sparkle_count):
        x = random.randint(0, w-1)
        y = random.randint(0, h-1)
        # Optional: only draw where alpha exists (around sprite)
        if alpha[y, x] > 0:
            offset_x = random.randint(-10, 10)
            offset_y = random.randint(-10, 10)
            generate_star(draw, x + offset_x, y + offset_y, radius=random.randint(1, 3), color=sparkle_color)

    # Merge: glow → sparkles → sprite
    combined = Image.alpha_composite(glow_img, sparkle_layer)
    final = Image.alpha_composite(combined, img)
    final.save(output_path, "PNG")

# Example usage
add_glow_and_sparkles("sprites/Kyurem.png", "GlitterKyurem.png")
