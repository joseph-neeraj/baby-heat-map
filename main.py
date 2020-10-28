import numpy
from PIL import Image, ImageDraw


def start():

    # Set values
    #----------------------------
    imageFile = 'sample.png'
    # Coordinates, where [0,0] is top left corner
    top_left_corner = [100, 100]  # [x, y]
    bottom_right_corner = [200, 200]  # [x, y]
    # ----------------------------

    # Preview area
    #----------------------------
    img = Image.open(imageFile)

    top_left_x = top_left_corner[0]
    top_left_y = top_left_corner[1]
    bottom_right_x = bottom_right_corner[0]
    bottom_right_y = bottom_right_corner[1]
    preview(img, top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    # ----------------------------

    # Calculate deviation
    # ----------------------------
    grayscale_image = Image.open(imageFile).convert('L') # [height, width]
    pixel_array = numpy.array(grayscale_image) / 255.0 # normalize
    print(f"Image file: {imageFile} , width x height : {pixel_array.shape}")

    sub_section = pixel_array[top_left_x:bottom_right_x, top_left_y:bottom_right_y]

    deviation = numpy.std(sub_section)

    print(f"Deviation: {deviation}")

    print('Done')

def preview(img, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    draw = ImageDraw.Draw(img)
    draw.rectangle((top_left_x, top_left_y, bottom_right_x, bottom_right_y), outline=255)
    img.save('preview.png')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
