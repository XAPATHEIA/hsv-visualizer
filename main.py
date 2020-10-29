import colorsys
import cv2
from PIL import Image as im
import numpy as np


# TODO: Might need to change img_init() to return a PIL image object instead of cv2 
#       so that I can read the pixel data and then construct using array.

# Check for valid file location, read using cv2
def img_init():
    return cv2.imread(input("Enter the path of the image you would like to convert to HSV: "))


base_img = img_init()


# User interface
def ui():
    try:
        choice = input("(E)dit HSV bands\n(C)onvert RGB image to HSV image\n").lower()
        return choice
    except ValueError as E:
        print(E)

        
# HSV Customization
def hsv_adjust():
    hsv_bands = ('hue', 'saturation', 'value')
    selection = input("Hue\nSaturation\nValue\nAll\nSelection: ").lower()
    if selection == 'all':
        altered_bands = []
        for channel in hsv_bands:
            if channel == hsv_bands[0]:
                altered_bands.append((int(input(f"{channel.upper()} (0-360): "))))
            else:
                altered_bands.append((int(input(f"{channel.upper()} (0-100): "))))
        return altered_bands
    else:
        return (selection, (int(input(f"{channel} (0-100): "))))



# Constructing HSV image
def construction(c, image):
    if c == 'c':
        hsv_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2HSV)
        return hsv_img
    if c == 'e':
        hsv = hsv_adjust()
        if len(hsv) == 3:
            pass
        else:
            pass




# Displaying the image
def image_display(final):
    cv2.imshow('Original Image', base_img)
    cv2.imshow('HSV image', final)

    # Wait for input to close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Executes code
def main():
    image_display(construction(ui(), base_img))


main()
