import cv2 as cv
import numpy as np

def pix_find(threshold,frame):
    height = frame.shape[0]
    width = frame.shape[1]
    print(height,width)
    for y in range(0,height):
        for x in range(0,width):
            frame[y,x] = 255 if frame[y,x] >= threshold else 0 
    return frame