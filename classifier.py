import cv2

from modules.tools import show_image_until_keypress

IMAGE_PATH = 'faces/Face 44.png'

def main():
    # Read in image with cv2
    original = cv2.imread(IMAGE_PATH)
    gray_image = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # contrast = increase_image_contrast(gray_image)
    show_image_until_keypress(gray_image)

    img_rows, img_cols = gray_image.shape

    print(img_rows, img_cols)

    # for row in img_rows:
    #     print(row)

    # trimmed_img = trim_image_padding(img)



if __name__ == '__main__':
    main()