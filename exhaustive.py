import numpy as np
import random
import math
import time
import cv2
from matplotlib import pyplot as plt


def main():
    ref = cv2.imread('ref.PNG', cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(ref, 'gray'), plt.title('ORIGINAL')
    plt.show()

    test = cv2.imread('test.PNG', cv2.IMREAD_GRAYSCALE)
    plt.plot(), plt.imshow(test, 'gray'), plt.title('ORIGINAL')
    plt.show()

    refx, refy = ref.shape
    testx, testy = test.shape

    print(refx)
    print(refy)
    print(testx)
    print(testy)

    lowest = float('inf')
    print(lowest)
    start = time.clock()
    for i in range(0, testx - refx + 1):
        for j in range(0, testy - refy + 1):
            test_interval = test[i:i + refx, j:j + refy]
            diff = test_interval - ref
            # print(diff)
            diff_sqr = np.sum(diff * diff)
            # print(diff_sqr)
            if diff_sqr < lowest:
                lowest = diff_sqr
                best = j, i
    end = time.clock()
    total_time = end - start
    print("Total Time ")
    print(total_time)
    print(best)
    print(lowest)

    res = cv2.matchTemplate(test, ref, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_loc)
    print(min_val)


if __name__ == "__main__":
    main()
