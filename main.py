from PIL import Image


# Check path eligibility
def path_check():
    return input("Input the path of the image you would like to convert:\n")


# Open image and convert to HSV
oi = Image.open(path_check()).convert('HSV')
pixel_data = list(oi.getdata())
print(pixel_data)
