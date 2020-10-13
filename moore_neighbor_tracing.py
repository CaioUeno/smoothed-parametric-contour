import numpy as np

# Next starting neighbor
def new_P(P):
    if P == 0 or P == 1:
        P = 7
    elif P == 2 or P == 3:
        P = 1
    elif P == 4 or P == 5:
        P = 3
    else: # P == 6 or P == 7
        P = 5
    return P

# Visit all neighbors to find the next pixel
def neighbor(img, row, col, P):
    list = [(row - 1, col), (row - 1, col + 1), (row, col + 1),
            (row + 1, col + 1), (row + 1, col), (row + 1, col - 1),
            (row, col - 1), (row - 1, col - 1)]
    for i in range(len(list)):
        ind = (i + P) % 8
        x, y = list[ind]
        if img[x, y] == 1:
            row = x
            col = y
            P = new_P(ind)
            break
    return row, col, P

# Find the contour
def image_contour(img):
    num_rows, num_cols = img.shape
    contour_row = []
    contour_col = []
    end = False

    for row in range(num_rows):
        for col in range(num_cols):
            if img[row, col] == 1:
                contour_row.append(row)
                contour_col.append(col)
                print(row, col)
                P = 2
                while True:
                    row, col, P = neighbor(img, row, col, P)
                    if contour_row[0] == row and contour_col[0] == col:
                        end = True
                        break
                    contour_row.append(row)
                    contour_col.append(col)
                    print(row, col)
            if end:
                break
        if end:
            break
    return contour_row, contour_col
