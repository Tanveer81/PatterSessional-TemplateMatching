import numpy as np
import random
import math
import time
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image


def main():
    a = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    lst = np.add(a, [(1, 1)])

    print(lst)


if __name__ == "__main__":
    main()
