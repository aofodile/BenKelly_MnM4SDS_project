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
    video_info = {'height':280,'width':360,'pad':20}
    def mainInner(video_info):
        hv = int(input("What would you like video height to be? "))
        wv = int(input("What would you like the video width to be? "))
        padv = int(input("What would you like the vidoe padding to be? "))
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
        frame = medfill(frame)
        ##frame = rolling_window(frame,4,1)
        ##frame = cont_maker(frame)
        ##frame = hsver(frame,fgbg)
        frame = hsver(frame)
        newframe = hougher(frame)
        frame = finder(frame)
        cv.imshow("Final",frame)
        cv.imshow("Houghs",newframe)
        if key == ord('q'):
            break
        elif key == ord('n'):
            mainInner(video_info)
    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/longgame_trim.mp4')
    main(cap)
    