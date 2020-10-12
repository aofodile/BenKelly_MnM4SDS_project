import cv2 as cv 
import numpy as np
from testhough import hough_maker
from testhsv import hsv_maker
from testinfo import info

def main(video):
    while True:
        ret,frame = video.read()
        if frame is None:
            break
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        hsvframe = hsv_maker(frame)
        houghframe = hough_maker(frame)
        cv.imshow("HSV",hsvframe)
        cv.imshow("Hough",houghframe)
        if key == ord('q') or key == 27:
            break
    video.release()
    cv.destroyAllWindows()

def testout(video):
    while True:
        ret,frame = video.read()
        if frame is None:
            print("Frame is None")
            break
        hsvframe = hough_maker(hsv_maker(frame))
        info(hsvframe)
        break

if __name__ == "__main__":
    video = cv.VideoCapture(r"../../footage/chipper.mp4")
    ##main(video)
    testout(video)