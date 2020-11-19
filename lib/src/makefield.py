import cv2 as cv
import numpy as np

def makefielder(image,coords,colorR, colorG, colorB, lineThickness):
    cv.line(image, coords[0], coords[1], (colorB, colorG, colorR), lineThickness)
    cv.line(image, coords[2], coords[3], (colorB, colorG, colorR), lineThickness)
    cv.line(image, coords[1], coords[2], (colorB, colorG, colorR), lineThickness)
    cv.line(image, coords[3], coords[0], (colorB, colorG, colorR), lineThickness)