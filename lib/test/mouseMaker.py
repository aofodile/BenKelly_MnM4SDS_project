import cv2 as cv 
import numpy as np
from basetest import mouseGet 
from testhsv import hsv_maker

import cv2 as cv
max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)

def transform(height,width,points,cap):
    window_detection_name = 'Video Capture'
    while True:
        ret,frame = cap.read()
        if frame is None:
            print("Frame is none")
            break
        psts1 = np.float32([[points[2],points[1],points[3],points[0]]])
        psts2 = np.float32([[800,400],[800,0],[0,400],[0,0]])
        mat = cv.getPerspectiveTransform(psts1,psts2)
        result = cv.warpPerspective(frame,mat,(800,400))
        cv.namedWindow(window_detection_name)
        cv.createTrackbar(low_H_name, window_detection_name , low_H, max_value_H, on_low_H_thresh_trackbar)
        cv.createTrackbar(high_H_name, window_detection_name , high_H, max_value_H, on_high_H_thresh_trackbar)
        cv.createTrackbar(low_S_name, window_detection_name , low_S, max_value, on_low_S_thresh_trackbar)
        cv.createTrackbar(high_S_name, window_detection_name , high_S, max_value, on_high_S_thresh_trackbar)
        cv.createTrackbar(low_V_name, window_detection_name , low_V, max_value, on_low_V_thresh_trackbar)
        cv.createTrackbar(high_V_name, window_detection_name , high_V, max_value, on_high_V_thresh_trackbar)
        key = cv.waitKey(10)
        if key == ord('p'):
            cv.waitKey(-1)
        frame_HSV = cv.cvtColor(result, cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
        cv.imshow('mert',frame_HSV)
        cv.imshow(window_detection_name,frame_threshold)
        if key == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    video = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    height,widths,points = mouseGet(video)
    cap = cv.VideoCapture(r'D:/Dev/gitVideo/pan_video.mp4')
    transform(height,widths,points,cap)