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
    #flat = field.makeAppField()
    #flatP = field.makepadding(flat)
    while True:
        flat = field.makeAppField()# Makes Field
        flatP = field.makepadding(flat)#
        ret,frame = video.read()#Reads in video file
        frame = warped(frame,points)#Video Warping Function
        if frame is None:#Stops code when video ends
            print("Frame is None")
            break
        key = cv.waitKey(10)
        if key == ord('p'):#Pauses video
            cv.waitKey(-1)
        processed = transform(frame)#Video Proccessing from lib/videoProcessing.py
        players,ball,coords = finder(processed)#Blob detection from lib/playerDetection.py
        fieldW = field.addplayers(coords,flatP)#Field object
        ##Shows Video Output
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
    ##Code is used to Cut field, and start the main application
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    info = {'height':280,'width':360,'pad':20}
    height,width,points = mouseGet(cap)
    info['height'] = 400
    info['width'] = 800
    video = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    main(video,info,points)