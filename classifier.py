import cv2

from modules.tools import show_image_until_keypress, make_img_black_and_white

IMAGE_PATH = 'faces/Face 44.png'

def main():
    # Read in image with cv2
    img = cv2.imread(IMAGE_PATH)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = make_img_black_and_white(img_gray)
    show_image_until_keypress(img)
    show_image_until_keypress(img_gray)

    num_rows, num_cols = img.shape

    top_left = img[0, 0]
    top_right = img[0, num_cols - 1]
    bottom_left = img[num_rows - 1, 0]
    bottom_right = img[num_rows - 1, num_cols - 1]

    # print('top_left = {}'.format(top_left))
    # print('top_right = {}'.format(top_right))
    # print('bottom_left = {}'.format(bottom_left))
    # print('bottom_right = {}'.format(bottom_right))
    print('number of rows: {}'.format(num_rows))
    print('number of cols: {}'.format(num_cols))

    for col in range(num_cols):

        col_sum = 0

        for row in range(num_rows):
            col_sum += img[row, col]

        print('avg of col {}: {}'.format(col + 1, col_sum / num_rows))


    # for row in img_rows:
    #     print(row)

    # trimmed_img = trim_image_padding(img)


if __name__ == '__main__':
    main()