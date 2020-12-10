import cv2 as cv 
import numpy as np
##Field Warping function
#########################
def warped(frame,points):
    psts1 = np.float32([[points[2],points[1],points[3],points[0]]])
    psts2 = np.float32([[800,400],[800,0],[0,400],[0,0]])
    mat = cv.getPerspectiveTransform(psts1,psts2)
    result = cv.warpPerspective(frame,mat,(800,400))
    return result