import cv2

def trim_image_padding(image):


    pass


def show_image_until_keypress(image):
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def make_img_black_and_white(image):
    (thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return im_bw
