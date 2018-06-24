import numpy as np
import time
import cv2
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from PIL import Image

test_image = 'fb.jpg'
ref_image = 'fb_ref.BMP'

def main():
    ref = cv2.imread(ref_image, cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(ref, 'gray'), plt.title('ORIGINAL')
    plt.show()

    test = cv2.imread(test_image, cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(test, 'gray'), plt.title('ORIGINAL')
    plt.show()

    ref_x, ref_y = ref.shape
    test_x, testy = test.shape

    print("Reference Image Dimension")
    print(ref_x)
    print(ref_y)
    print("Test Image Dimension")
    print(test_x)
    print(testy)

    lowest = float('inf')
    # print(lowest)
    start = time.clock()
    limit_x = test_x - ref_x + 1
    limit_y = testy - ref_y + 1
    for i in range(0, limit_x):
        for j in range(0, limit_y):
            end_x = i + ref_x
            end_y = j + ref_y
            test_interval = test[i:end_x, j:end_y]
            diff = test_interval - ref
            # print(diff)
            diff_sqr = np.sum(diff * diff)
            # print(diff_sqr)
            if lowest > diff_sqr:
                lowest = diff_sqr
                best_x = i
                best_y = j
    end = time.clock()
    total_time = end - start
    print("Total Time ")
    print(total_time)
    
    print("Printing My Result ")
    print(best_x)
    print(best_y)
    print(lowest)

    # test = cv2.imread('test.PNG', cv2.IMREAD_GRAYSCALE)
    # plt.plot(), plt.imshow(test, 'gray'), plt.title('ORIGINAL')
    # plt.plot(i, j, 'o')
    # plt.show()

    im = np.array(Image.open(test_image), dtype=np.uint8)
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
