import cv2 as cv
import numpy as np

def hsv_maker(video):
    low = {"H":32,"S":80,"V":62}
    high = {"H":114,"S":255,'V':132}
    frame_HSV = cv.cvtColor(video,cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV,(low["H"],low["S"],low["V"]),(high["H"],high['S'],high["V"]))
    return frame_threshold
