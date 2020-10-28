import numpy
from PIL import Image, ImageDraw


def start():
    # ----------------------------
    # Set values
    # ----------------------------
    image_file = 'sample.png'
    # Coordinates, where [0,0] is top left corner
    top_left_corner = [100, 100]  # [x, y]
    bottom_right_corner = [200, 200]  # [x, y]
    # ----------------------------

    # ----------------------------
    # Preview area
    # ----------------------------
    img = Image.open(image_file)

    top_left_x = top_left_corner[0]
    top_left_y = top_left_corner[1]
    bottom_right_x = bottom_right_corner[0]
    bottom_right_y = bottom_right_corner[1]

    draw = ImageDraw.Draw(img)
    draw.rectangle((top_left_x, top_left_y, bottom_right_x, bottom_right_y), outline=255)
    img.save('preview.png')
    # ----------------------------

    # ----------------------------
    # Calculate deviation
    # ----------------------------
    grayscale_image = Image.open(image_file).convert('L')
    pixel_array = numpy.array(grayscale_image) / 255.0 # normalize
    print(f"Image file: {image_file} , height x width : {pixel_array.shape}")

    sub_section = pixel_array[top_left_x:bottom_right_x, top_left_y:bottom_right_y]

    deviation = numpy.std(sub_section)

    print(f"Deviation: {deviation}")

    print('Done')


if __name__ == '__main__':
    start()
