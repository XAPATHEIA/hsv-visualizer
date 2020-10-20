from PIL import Image as im


# Create image and convert to HSV
def image_define():
    img = im.new('RGB', (160, 120), color='white')
    pixel_data = list((img.convert('HSV')).getdata())  # Converting to HSV, reading pixels


# Collect user defined HSV values
def user_hsv():
    hsv_channels = ('HUE', 'SATURATION', 'VALUE')
    user_hsv_values = []

    for channel in hsv_channels:
        try:
            user_hsv_values.append(int(input(f"{channel}: ")))
        except ValueError:
            exit()

    return user_hsv_values


# Convert image to reflect user defined HSV values
def hsv_construction(hsv):
    return im.fromarray((hsv[0], hsv[1], hsv[2]))


def main():
    hsv_construction(user_hsv())

main()