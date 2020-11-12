import colorsys
import cv2
from PIL import Image as im
import numpy as np


hsv_bands = ('hue', 'saturation', 'value')


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
    selection = input("Hue\nSaturation\nValue\nAll\nSelection: ").lower()
    if selection == 'all':
        altered_bands = []
        for channel in hsv_bands:
            if channel == 'hue':
                altered_bands.append((int(input(f"{channel.upper()} (0-360): "))))
            else:
                altered_bands.append((int(input(f"{channel.upper()} (0-100): "))))
        return selection, altered_bands
    else:
        if selection == 'hue':
            return (selection, (int(input(f"{selection} (0-360): "))))
        else:
            return (selection, (int(input(f"{selection} (0-100): "))))



# Constructing HSV image
def construction(c, image):
    if c == 'c':
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return hsv_img
    if c == 'e':
        selection, altered_bands = hsv_adjust()
        if selection == 'all':
            for band, alteration in enumerate(altered_bands):
                image[:,:,band] = alteration
            return image
        else:
            h_s_v = hsv_bands.index(selection)
            image[:,:,h_s_v] = altered_bands
            return image


# Displaying the image
def image_display(final):
    cv2.imshow('HSV image', final)

    # Wait for input to close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Executes code
def main():
    image_display(construction(ui(), base_img))


main()
