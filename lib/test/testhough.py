import cv2 as cv
import numpy as np

def hough_maker(frame):
    canimg = cv.Canny(frame,50,200)
    lines = cv.HoughLines(canimg,1,np.pi/180,120,np.array([]))
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 -1000*(-b))
        y2 = int(y0 - 1000 *(1))
        cv.line(frame, (x1,y1), (x2,y2), (0,0,255), 2)
    return canimg
