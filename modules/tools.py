import cv2


def trim_image_padding(binary_img):
    num_rows, num_cols = binary_img.shape

    top_left = binary_img[0, 0]
    top_right = binary_img[0, num_cols - 1]
    bottom_left = binary_img[num_rows - 1, 0]
    bottom_right = binary_img[num_rows - 1, num_cols - 1]

    col_trim_start = 1  # first col
    col_trim_end = num_cols  # last col
    row_trim_start = 1  # first col
    row_trim_end = num_rows # last col

    # find col_trim_start
    for col in range(num_cols):
        col_sum = 0
        for row in range(num_rows):
            col_sum += binary_img[row, col]

        avg_of_col = col_sum / num_rows
        if avg_of_col == 255:  # if all white, move on to next column
            continue
        else:
            col_trim_start = col  # else, this column # is where we trim at
            break

    # find col_trim_end
    for col in range(num_cols-1, -1, -1):
        col_sum = 0
        for row in range(num_rows):
            col_sum += binary_img[row, col]

        avg_of_col = col_sum / num_rows
        if avg_of_col == 255:  # if all white, move on to next column
            continue
        else:
            col_trim_end = col  # else, this column # is where we trim at
            break

    # find row_trim_start
    for row in range(num_rows):
        row_sum = 0
        for col in range(num_cols):
            row_sum += binary_img[row, col]

        avg_of_rows = row_sum / num_cols
        if avg_of_rows == 255:  # if all white, move on to next row
            continue
        else:
            row_trim_start = row  # else, this row # is where we trim at
            break

    # find row_trim_end
    for row in range(num_rows - 1, -1, -1):
        row_sum = 0
        for col in range(num_cols):
            row_sum += binary_img[row, col]

        avg_of_rows = row_sum / num_cols
        if avg_of_rows == 255:  # if all white, move on to next row
            continue
        else:
            row_trim_end = row  # else, this row # is where we trim at
            break

    # print('image dimensions: height={} x width={}'.format(num_rows, num_cols))
    # print('col_trim_start: {}'.format(col_trim_start))
    # print('col_trim_end: {}'.format(col_trim_end))
    # print('row_trim_start: {}'.format(row_trim_start))
    # print('row_trim_end: {}'.format(row_trim_end))

    # pixels_width_to_crop = col_trim_end-col_trim_start
    # pixels_height_to_crop = row_trim_end-row_trim_start

    trimmed = binary_img[row_trim_start-1:row_trim_end, col_trim_start-1:col_trim_end] # Crop from x, y, w, h -> 100, 200, 300, 400
    return trimmed


def show_image_until_keypress(image):
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def make_img_black_and_white(image):
    (thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return im_bw


def initialize_layer(img):

    num_rows, num_cols = img.shape

    for row in range(num_rows):
        for col in range(num_cols):
            print(img[row, col])