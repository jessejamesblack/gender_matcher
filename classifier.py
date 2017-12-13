import cv2

from modules.tools import trim_image_padding

IMAGE_PATH = 'faces/Face 1.png'

def main():
    # Read in image with cv2
    img = cv2.imread(IMAGE_PATH)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # First, process the image so that extra white space is removed.
    trimmed_img = trim_image_padding(img)



if __name__ == '__main__':
    main()