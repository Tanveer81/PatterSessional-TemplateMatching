import numpy as np
import time
import cv2
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from PIL import Image

test_image = 'sea.bmp'
ref_image = 'ref.bmp'
hierarchy = 3

def main():
    ref = cv2.imread(ref_image, cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(ref, 'gray'), plt.title('ORIGINAL')
    plt.show()

    test = cv2.imread(test_image, cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(test, 'gray'), plt.title('ORIGINAL')
    plt.show()

    ref_x, ref_y = ref.shape
    test_x, test_y = test.shape
    # test_x = int(np.ceil(test_x / 2))
    # test_y = int(np.ceil(test_y / 2))
    # ref_x = int(np.ceil(ref_x / 2))
    # ref_y = int(np.ceil(ref_y / 2))

    test1 = cv2.resize(test, (int(np.ceil(test_x / 2**hierarchy)), int(np.ceil(test_y / 2**hierarchy))), interpolation=cv2.INTER_CUBIC)
    ref1 = cv2.resize(ref, (int(np.ceil(ref_x / 2**hierarchy)), int(np.ceil(ref_y / 2**hierarchy))), interpolation=cv2.INTER_CUBIC)

    print("Reference Image Dimension")
    print(ref_x)
    print(ref_y)
    print("Test Image Dimension")
    print(test_x)
    print(test_y)

    lowest = float('inf')
    # print(lowest)
    start = time.clock()
    limit_x = int(np.ceil(test_x / 2**hierarchy)) - int(np.ceil(ref_x / 2**hierarchy)) + 1
    limit_y = int(np.ceil(test_y / 2**hierarchy)) - int(np.ceil(ref_y / 2**hierarchy)) + 1
    print(limit_x)
    print(limit_y)
    for i in range(0, limit_x):
        for j in range(0, limit_y):
            end_x = i + int(np.ceil(ref_x / 2**hierarchy))
            end_y = j + int(np.ceil(ref_y / 2**hierarchy))
            test_interval = test1[j:end_y, i:end_x]
            diff = test_interval - ref1
            diff_sqr = np.sum(diff * diff)
            if lowest > diff_sqr:
                lowest = diff_sqr
                best_x = i
                best_y = j

    # best_x = best_x * 2**hierarchy
    # best_y = best_y * 2**hierarchy

    a = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    lst = []
    for i in range(0, hierarchy):
        best_x = best_x * 2
        best_y = best_y * 2
        test1 = cv2.resize(test, (int(np.ceil(test_x / 2**(hierarchy - i-1))), int(np.ceil(test_y / 2**(hierarchy - i-1)))), interpolation=cv2.INTER_CUBIC)
        ref1 = cv2.resize(ref, (int(np.ceil(ref_x / 2**(hierarchy - i-1))), int(np.ceil(ref_y / 2**(hierarchy - i-1)))), interpolation=cv2.INTER_CUBIC)
        lst = np.add(a, [(best_x, best_y)])
        for point in lst:
            end_x = point[0] + int(np.ceil(ref_x / 2**(hierarchy - i-1)))
            end_y = point[1] + int(np.ceil(ref_y / 2**(hierarchy - i-1)))

            if end_x > int(np.ceil(test_x / 2**(hierarchy - i-1))) or end_y > int(np.ceil(test_y / 2**(hierarchy - i-1))):
                continue

            test_interval = test1[point[1]:end_y, point[0]:end_x]
            diff = test_interval - ref1
            # print(diff)
            diff_sqr = np.sum(diff * diff)
            # print(diff_sqr)
            if lowest > diff_sqr:
                lowest = diff_sqr
                best_x = point[0]
                best_y = point[1]

    end = time.clock()
    total_time = end - start
    print("Total Time ")
    print(total_time)

    print("Printing My Result ")
    print(best_x)
    print(best_y)
    print(lowest)

    im = np.array(Image.open(test_image), dtype=np.uint8)
    fig, ax = plt.subplots(1)
    ax.imshow(im)
    rect = patches.Rectangle((best_x, best_y), ref_y, ref_x, linewidth=3, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.show()

    print("Printing open-cv result")
    res = cv2.matchTemplate(test, ref, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_loc)
    print(min_val)


if __name__ == "__main__":
    main()
