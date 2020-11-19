import cv2 as cv
import numpy as np
from blob import finder
from hough import hougher
from track import tracker
from hsv import hsver
from rollwind import rolling_window
from med import medfill
from makefield import makefielder

def main(video,info):
    src_window = "Source"
    dst_window ="Output"
    def infoGetter(info):
        hv = int(input("What would you like video height to be? "))
        wv = int(input("What would you like the video width to be? "))
        padv = int(input("What would you like the vidoe padding to be? "))
        info['height'] = hv
        info['width'] = wv
        info['pad'] = padv
        return info
    minField = info["width"]*.2 * info['height']*1
    field = np.zeros((info['height'] + info['pad']*2,info['width'] + info['pad']*2,3),np.uint8)
    (xb1, yb1) = (info['pad'], info['pad'])
    (xb2, yb2) = (info['pad'] + info['width'], info['pad'])
    (xb3, yb3) = (info['pad'] + info['width'], info['pad'] + info['height'])
    (xb4, yb4) = (info['pad'], info['pad'] + info['height'])
    makefielder(field,[(xb1, yb1),(xb2, yb2),(xb3, yb3),(xb4, yb4)],0,255,0,2)
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
        cv.imshow("Blank",field)
        cv.imshow("Final",frame)
        ##cv.imshow("Houghs",newframe)
        if key == ord('q'):
            break
        elif key == ord('n'):
            info = infoGetter(info)
    video.release()
    cv.destroyAllWindows()
##########################
if __name__ == "__main__":
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/longgame_trim.mp4')
    info = {'height':280,'width':360,'pad':20}
    main(cap,info)
    