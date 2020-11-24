import cv2 as cv 
import numpy as np
from basetest import mouseGet 

def transform(height,width,points,cap):
    while True:
        ret,frame = cap.read()
        if frame is None:
            print("Frame is none")
            break
        psts1 = np.float32([[points[2],points[1],points[3],points[0]]])
        psts2 = np.float32([[800,400],[800,0],[0,400],[0,0]])
        mat = cv.getPerspectiveTransform(psts1,psts2)
        result = cv.warpPerspective(frame,mat,(800,400))
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        cv.imshow('Frame',frame)
        cv.imshow('mert',result)
        if key == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    video = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    height,widths,points = mouseGet(video)
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    transform(height,widths,points,cap)