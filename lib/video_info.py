import cv2 
import numpy as np

def getinfo(video):
    width = video.get(3)
    height = video.get(4)
    return width,height
