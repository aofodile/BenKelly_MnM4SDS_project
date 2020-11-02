import cv2 as cv
import numpy as np
from blob import finder
from hough import hougher
from track import tracker
from hsv import hsver
from rollwind import rolling_window
from med import medfill
##from contour import cont_maker

def main(video):
    src_window = "Source"
    dst_window ="Output"
    while True:
        ret,frame = video.read()
        if frame is None:
            print("Frame is None")
            break
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        ##frame = medfill(frame)
        ##frame = rolling_window(frame,4,1)
        ##frame = cont_maker(frame)
        frame = hsver(frame)
        newframe = hougher(frame)
        frame = finder(frame)
        cv.imshow("Final",frame)
        cv.imshow("Houghs",newframe)
        if key == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/longgame_trim.mp4')
    main(cap)
    