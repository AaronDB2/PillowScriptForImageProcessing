from PIL import Image
from ImageProcessing import *
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments provided.")
    else:
        image_path = sys.argv[1]
        img = Image.open(image_path)
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)

        print("Hello Welcom to ImageProcessing")
        print(
            """
            1: Gray scale
            2: Draw circle
            3: Write on image
            4: Invert image color
            """
        )
        operation_number = input("Give the number of the operation you want to do: ")

        try:
            operation_number_converted = int(operation_number)
            if operation_number_converted == 1:
                print("Gray scale")
                gray = grayscale(img)
                gray.show()
                gray.save(f"./savedImages/{name}_gray.jpg")
            elif operation_number_converted == 2:
                print("Draw circle")
                circle_image = draw_circle_on_image(img)
                circle_image.show()
                circle_image.save(f"./savedImages/{name}_circle_image.jpg")
            elif operation_number_converted == 3:
                print("Write on image")
                text_image = write_on_image(img)
                text_image.show()
                text_image.save(f"./savedImages/{name}_text_image.jpg")
            elif operation_number_converted == 4:
                print("Invert image color")
                inverted_image = invert_image_color(img)
                inverted_image.show()
                inverted_image.save(f"./savedImages/{name}_inverted_image.jpg")
            else:
                print("Number not recognized")
        except ValueError:
            print("That's not a Number.")