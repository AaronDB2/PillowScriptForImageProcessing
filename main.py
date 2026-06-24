from PIL import Image
from ImageProcessing import *

if __name__ == "__main__":
    img = Image.open("./images/Pickachu.jpg")

    inverted_image = invert_image_color(img)
    inverted_image.show()
    img.show()

    circle_image = draw_circle_on_image(inverted_image)
    circle_image.show()

    gray = grayscale(img)
    gray.show()

    text_image = write_on_image(gray)
    text_image.show()