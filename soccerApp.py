import cv2 as cv
import numpy as np
from twoDfield import Field
from lib.videoProcessing import transform
from lib.playerDetection import finder
from lib.video_info import getinfo
#####################
def main(video,info):
    src_window = "Source"
    dst_window ="Output"
    field = Field(info)
    flat = field.makeAppField()
    flatP = field.makepadding(flat)
    width,height = getinfo(video)
    while True:
        ret,frame = video.read()
        if frame is None:
            print("Frame is None")
            break
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        processed = transform(frame)
        players,ball,coords = finder(processed)
        #cv.imshow(dst_window,flatP)
        cv.imshow("Players",players)
        #cv.imshow("Ball",ball)
        if key == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()
###########################
if __name__  == "__main__":
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/longgame_trim.mp4')
    info = {'height':280,'width':360,'pad':20}
    main(cap,info)