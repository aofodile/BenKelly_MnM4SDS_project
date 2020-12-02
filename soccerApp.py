import cv2 as cv
import numpy as np
from twoDfield import Field
from lib.videoProcessing import transform
from lib.playerDetection import finder
from lib.video_info import getinfo
from lib.mousefield import mouseGet
from lib.warpfield import warped
#####################
def main(video,info,points):
    ##src_window = "Source"
    dst_window ="Output"
    field = Field(info)
    ##flat = field.makeAppField()
    ##flatP = field.makepadding(flat)
    while True:
        flat = field.makeAppField()
        flatP = field.makepadding(flat)
        ret,frame = video.read()
        frame = warped(frame,points)
        if frame is None:
            print("Frame is None")
            break
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        processed = transform(frame)
        players,ball,coords = finder(processed)
        fieldW = field.addplayers(coords,flatP)
        cv.imshow(dst_window,fieldW)
        cv.imshow("Players",players)
        cv.imshow("Source_Warped",frame)
        #cv.imshow("Ball",ball)
        if key == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()
###########################
if __name__  == "__main__":
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    info = {'height':280,'width':360,'pad':20}
    height,width,points = mouseGet(cap)
    info['height'] = 400
    info['width'] = 800
    video = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    main(video,info,points)