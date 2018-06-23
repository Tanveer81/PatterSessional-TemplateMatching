import numpy as np
import random
import math
import time
import cv2
from matplotlib import pyplot as plt


def main():
    list = [(0,0)]

    neighbour_x = 1
    neighbour_y = 2
    neighbour = (neighbour_x, neighbour_y)
    list.append(neighbour)

    neighbour_x = 3
    neighbour_y = 4
    neighbour = (neighbour_x, neighbour_y)
    list.append(neighbour)

    for a in list:
        print(a)


if __name__ == "__main__":
    main()
