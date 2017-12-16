import cv2
from modules.tools import *

IMAGE_PATH = 'faces/Face 6.png'

class SimpleNeuron(object):
    def __init__(self):
        self.input_value = 0
        self.weight = 0.5

    def update_weight(self, weight):
        self.weight = weight

    def change_input(self, amended):
        self.input_value = amended

def main():
    # Read in image with cv2
    original_img = cv2.imread(IMAGE_PATH)

    # Convert to greyscale
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    # Convert to binary
    binary_img = make_img_black_and_white(gray_img)

    # Trim this image until only
    trimmed_img = trim_image_padding(binary_img)

    # show_image_until_keypress(binary_img)
    show_image_until_keypress(trimmed_img)
    cv2.imwrite('trimmed.png', trimmed_img)

    initialize_layer(trimmed_img)



if __name__ == '__main__':
    main()