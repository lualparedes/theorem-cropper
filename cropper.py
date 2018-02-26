from PIL import Image



# Import the image
input_img = Image.open("input_img.png")



# Find the coordinate with the first non-white pixel starting from all four sides
def get_left(img, width, height):

    pixel_found = False

    for col in range(width):
        if (pixel_found):
            break
        for row in range(height):
            if (
                img.getpixel((col,row))[0] != 255 or
                img.getpixel((col,row))[1] != 255 or
                img.getpixel((col,row))[2] != 255
            ):
                left = col
                pixel_found = True
                break
            
    return left


def get_top(img, width, height):

    pixel_found = False

    for row in range(height):
        if (pixel_found):
            break
        for col in range(width):
            if (
                img.getpixel((col,row))[0] != 255 or
                img.getpixel((col,row))[1] != 255 or
                img.getpixel((col,row))[2] != 255
            ):
                top = row
                pixel_found = True
                break
            
    return top


def get_right(img, width, height):

    pixel_found = False

    for col in reversed(range(width)):
        if (pixel_found):
            break
        for row in range(height):
            if (
                img.getpixel((col,row))[0] != 255 or
                img.getpixel((col,row))[1] != 255 or
                img.getpixel((col,row))[2] != 255
            ):
                right = col + 1
                pixel_found = True
                break
            
    return right


def get_bottom(img, width, height):

    pixel_found = False

    for row in reversed(range(height)):
        if (pixel_found):
            break
        for col in range(width):
            if (
                img.getpixel((col,row))[0] != 255 or
                img.getpixel((col,row))[1] != 255 or
                img.getpixel((col,row))[2] != 255
            ):
                bottom = row + 1
                pixel_found = True
                break
            
    return bottom


def get_coordinates(img):  

    coordinates = []
    width = img.size[0]
    height = img.size[1]

    coordinates.append(get_left(img, width, height))
    coordinates.append(get_top(img, width, height))
    coordinates.append(get_right(img, width, height))
    coordinates.append(get_bottom(img, width, height))

    return coordinates


crop_coordinates = get_coordinates(input_img)



# Crop the picture using the coordinates found
output_img = input_img.crop((
        crop_coordinates[0], 
        crop_coordinates[1], 
        crop_coordinates[2], 
        crop_coordinates[3]
    ))



# Export the image
output_img.save("output_img.png")