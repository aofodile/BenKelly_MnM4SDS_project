import cv2 as cv
import numpy as np

def cont_make(frame):
    ret, thresh = cv.threshold(frame,127,255,0)
    contours,hierarchy = cv.findContours(thresh,2,1)
    cont = contours[0]
    rect = cv.minAreaRect(cont)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(frame,[box],0,(0,0,255),2)
    return frame

if __name__ == "__main__":
    video = cv.VideoCapture(r"../../footage/chipper.mp4")
    main(video)
