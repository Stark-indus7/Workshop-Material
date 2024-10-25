# This is the main Python file for the Image Resizer and Converter project.
from PIL import Image

def resize_image(input_image, output_image, size):
    image = Image.open(input_image)
    image = image.resize(size)
    image.save(output_image)
    print(f"Image saved as {output_image}.")

input_image = input("Enter image path: ")
output_image = input("Enter output path: ")
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))
resize_image(input_image, output_image, (width, height))
