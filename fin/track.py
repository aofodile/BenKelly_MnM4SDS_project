import cv2 as cv
import numpy as np

def tracker(video,num=3):
    track_xl = cv.MultiTracker_create()
    tri_dic = {'csrt':cv.TrackerCSRT_create,'kcf':cv.TrackerKCF_create,
                'boosting' : cv.TrackerBoosting_create,'mil': cv.TrackerMIL_create}
    ret, frame = video.read()
    for i in range(num):
        cv.imshow("Frame",frame)
        rec = cv.selectROI("Frame",frame)
        track = tri_dic["csrt"]()
        track_xl.add(track,frame,rec)
    return track_xl