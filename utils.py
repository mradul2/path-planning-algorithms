import numpy as np 
import cv2 
import math 
import time 
from queue import PriorityQueue
import os 

# Please change the Image path according to you if error is coming
img_path = os.path.join(os.getcwd(),"Task_1_Low.png")
IMAGE = cv2.imread(img_path)
if IMAGE is None:
    print("Cannot read the Image!!")
    exit()


# Different Modes for Node class 
START = 0
END = 1
OBSTACLE = 2
NAVIGABLE = 3
CLOSED = 4
OPEN = 5
PATH = 6


# Size and Upscale Utils 
SIZE = 100
UPSCALE = 10


# Exact pixel colors in the given Image 
GREEN = np.array([113,204,45]).astype("uint8")
RED = np.array([60,76,231]).astype("uint8")
BLACK = np.array([0,0,0]).astype("uint8")
WHITE = np.array([255,255,255]).astype("uint8")
ORANGE = np.array([0,69,255]).astype("uint8")
BLUE = np.array([230,216,173]).astype("uint8")
PURPLE = np.array([139,0,0]).astype("uint8")

# Function to Upscale the Image and for finally showing it 
def upScale(orig_img: np.ndarray = None, shape: tuple = None) -> np.ndarray:

    img = orig_img.copy()
    (h, w, d) = img.shape
    (hF, wF, dF) = shape

    hR = hF // h
    wR = wF // w

    upscale_img = np.ndarray(shape, dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            upscale_img[hR*i:hR*i+hR,wR*j:wR*j+wR,:] = img[i,j,:]

    return upscale_img

# Utility function to show Image in between running Algorithm 
def show(matrix,IMAGE):
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j].mode == OPEN:
                IMAGE[i,j] = BLUE
            elif matrix[i][j].mode == CLOSED:
                IMAGE[i,j] = ORANGE
            elif matrix[i][j].mode == PATH:
                IMAGE[i][j] = PURPLE

    cv2.imshow("SHOW", upScale(IMAGE,(1000,1000,3)))
    cv2.waitKey(1)
