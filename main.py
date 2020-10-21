from PIL import Image as im
import cv2
from cv2 import error


# Check for valid file location, read using cv2
def img_init():
    try:
        img = cv2.imread(input("Enter the path of the image you would like to convert to HSV: "))
        return img
    except:
        print("Incorrect Path")


base_img = img_init()


# User interface
def ui():
    try:
        choice = input("HSV) Edit HSV bands\nRGB) Convert RGB to HSV\n")
        return choice
    except ValueError as E:
        print(E)


# HSV Customization
def hsv_adjust():
    hsv_bands = ('HUE', 'SATURATION', 'VALUE')
    altered_bands = []
    for channel in hsv_bands:
        try:
            altered_bands.append(int(input(f"{channel} (0-3): ")))
        except ValueError as E:
            print(E)
    return altered_bands


# Constructing HSV image
def construction(c, image):
    if c == 'RGB':
        hsv_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2HSV)
        return hsv_img
    if c == 'HSV':
        try:
            hsv = hsv_adjust()
            new_hsv = image[:,:hsv[2]]
            return new_hsv
        except IndexError:
            print("Inputted HSV Band Integer out of range")


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
