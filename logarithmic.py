import numpy as np
import random
import math
import time
import cv2
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from PIL import Image


def main():
    ref = cv2.imread('ref.BMP', cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(ref, 'gray'), plt.title('ORIGINAL')
    plt.show()

    test = cv2.imread('sea.BMP', cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(test, 'gray'), plt.title('ORIGINAL')
    plt.show()

    ref_x, ref_y = ref.shape
    test_x, test_y = test.shape

    print("Reference Image Dimension")
    print(ref_x)
    print(ref_y)
    print("Test Image Dimension")
    print(test_x)
    print(test_y)

    lowest = float('inf')
    start = time.clock()

    a = [-1, 0, 1]
    kx = math.log2(test_x/2)
    kx = math.floor(kx)
    ky = math.log2(test_y/2)
    ky = math.floor(ky)
    dx = int(math.pow(2, kx - 1))
    dy = int(math.pow(2, ky - 1))
    center_x = math.ceil(test_x / 2)
    center_y = math.ceil(test_y / 2)
    # print(dx)
    # print(dy)
    center = (center_x, center_y)
    # print(center)
    best = center
    best_x = 0
    best_y = 0
    while dx >= 1.0 and dy >= 1.0:
        lst = [best]
        for i in a:
            for j in a:
                neighbour_x = center_x + i * dx
                neighbour_y = center_y + j * dy
                neighbour = (neighbour_x, neighbour_y)
                lst.append(neighbour)
        dx = int(dx / 2)
        dy = int(dy / 2)
        # print(lst)


        for point in lst:
            end_x = point[0] + ref_x
            end_y = point[1] + ref_y

            if end_x > test_x or end_y > test_y:
                continue

            test_interval = test[point[0]:end_x, point[1]:end_y]
            diff = test_interval - ref
            # print(diff)
            diff_sqr = np.sum(diff * diff)
            # print(diff_sqr)
            if lowest > diff_sqr:
                lowest = diff_sqr
                best_x = point[0]
                best_y = point[1]

        best = (best_x, best_y)

    end = time.clock()
    total_time = end - start
    print("Total Time ")
    print(total_time)

    print("Printing My Result ")
    print(best_x)
    print(best_y)
    print(lowest)


    # test = cv2.imread('sea.BMP', cv2.IMREAD_GRAYSCALE)
    # plt.plot(), plt.imshow(test, 'gray'), plt.title('ORIGINAL')
    # plt.plot(best_y, best_x, 'o')
    # plt.show()

    im = np.array(Image.open('sea.bmp'), dtype=np.uint8)
    # Create figure and axes
    fig, ax = plt.subplots(1)
    # Display the image
    ax.imshow(im)
    # Create a Rectangle patch
    rect = patches.Rectangle((best_y, best_x), ref_y, ref_x, linewidth=3, edgecolor='r', facecolor='none')
    # Add the patch to the Axes
    ax.add_patch(rect)
    plt.show()


    print("Printing open-cv result")
    res = cv2.matchTemplate(test, ref, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_loc)
    print(min_val)


if __name__ == "__main__":
    main()
