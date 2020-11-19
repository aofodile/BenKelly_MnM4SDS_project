import cv2 as cv 
import numpy as np

def finder(frame):
    playerframe = playerfind(frame)
    ballframe = ballfind(playerframe)
    return ballframe

def playerfind(frame):
    ##Params
    params = cv.SimpleBlobDetector_Params()
    params.minThreshold = 100
    params.maxThreshold = 1000
    params.filterByArea = True
    params.minArea = 200
    params.filterByColor = True
    params.blobColor = 0
    params.filterByCircularity = True
    params.minCircularity = 0.1
    params.filterByConvexity = True
    params.minConvexity = 0.1
    params.filterByInertia = True
    params.minInertiaRatio = 0.002
    ###Blob finding
    playerdetector = cv.SimpleBlobDetector_create(params)
    player_points = playerdetector.detect(frame)
    player_keys = cv.drawKeypoints(frame, player_points, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return player_keys

def ballfind(frame):
    params = cv.SimpleBlobDetector_Params()
    params.minThreshold = 50
    params.maxThreshold = 1000
    params.filterByArea = True
    params.minArea = 30
    params.maxArea = 75
    params.filterByColor = True
    params.blobColor = 0
    params.filterByCircularity = True
    params.minCircularity = 0.01
    balldetector = cv.SimpleBlobDetector_create(params)
    ball_points = balldetector.detect(frame)
    try:
        if np.max(ball_points) is not None:
            ball_keys = cv.drawKeypoints(frame, np.max(ball_points), np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        else:
            ball_keys = cv.drawKeypoints(frame, ball_points, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    except:
        ball_keys = cv.drawKeypoints(frame, ball_points, np.array([]), (0,255,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return ball_keys

