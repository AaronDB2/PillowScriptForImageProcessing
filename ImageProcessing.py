from typing import Any

from PIL import ImageDraw, ImageFont

# Invert colors on an Image
def invert_image_color(image):
    editable_image = image.copy()
    pixels = editable_image.load()
    # Loop over all pixels and get the RGB values.
    for x in range(editable_image.width):
        for y in range(editable_image.height):
            r, g, b = pixels[x, y]

            # Invert the RGB Values
            pixels[x, y] = (
                255 - r,
                255 - g,
                255 - b,
            )
    return editable_image

# Draw a circle on an Image
def draw_circle_on_image(image):
    editable_image = image.copy()
    draw = ImageDraw.Draw(editable_image)

    bottom, left, right, top = calculate_image_center(editable_image)

    draw.ellipse(
        (left, top, right, bottom),
        fill="red"
    )

    return editable_image

# Convert image to grayscale
def grayscale(image):
    editable_image = image.copy()
    editable_image = editable_image.convert("L")
    return editable_image

# Write on image
def write_on_image(image):
    editable_image = image.copy()
    draw = ImageDraw.Draw(editable_image)
    font = ImageFont.truetype("arial.ttf", 40)

    bottom, left, right, top = calculate_image_center(editable_image)

    draw.text(
        (left, right),
        "Hello",
        font=font
    )
    return editable_image

def calculate_image_center(editable_image) -> tuple[Any, Any, Any, Any]:
    # Circle settings
    radius = 50

    # Find the center of the image
    center_x = editable_image.width // 2
    center_y = editable_image.height // 2

    # Bounding box for the circle
    left = center_x - radius
    top = center_y - radius
    right = center_x + radius
    bottom = center_y + radius
    return bottom, left, right, top