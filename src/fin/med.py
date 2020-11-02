import numpy as np
import cv2 as cv

def medfill(frame):
    median = cv.medianBlur(frame,3)
    return median
