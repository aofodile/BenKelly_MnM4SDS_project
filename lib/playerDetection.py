import cv2 as cv 
import numpy as np
#Function, and methods for the player, and ball detection
##################
def finder(frame):
    playerframe,playerCoords = playerfind(frame)
    ballframe,ballCoords = ballfind(frame)
    coords = {"players":playerCoords,"ball":ballCoords}
    return playerframe,ballframe,coords
######################
def playerfind(frame):
    ##Params
    params = cv.SimpleBlobDetector_Params()
    params.minThreshold = 50
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 75
    params.filterByColor = True
    params.blobColor = 0
    params.filterByCircularity = True
    params.minCircularity = 0.2
    params.filterByConvexity = True
    params.minConvexity = 0.2
    params.filterByInertia = True
    params.minInertiaRatio = 0.002
    ###Blob finding
    playerdetector = cv.SimpleBlobDetector_create(params)
    player_points = playerdetector.detect(frame)
    playerCoords = []
    for coords in player_points:
        playerCoords.append([coords.pt[0],coords.pt[1]])
    ##print("Player Points x:",player_points[0].pt[0])
    ##print("Player Points y:",player_points[0].pt[1])
    player_keys = cv.drawKeypoints(frame, player_points, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return player_keys,playerCoords

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
    ballCoords = []
    for coords in ball_points:
        ballCoords.append([coords.pt[0],coords.pt[1]])
    try:
        if np.max(ball_points) is not None:
            ball_keys = cv.drawKeypoints(frame, np.max(ball_points), np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        else:

            ball_keys = cv.drawKeypoints(frame, ball_points, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    except:
        ball_keys = cv.drawKeypoints(frame, ball_points, np.array([]), (0,255,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return ball_keys,ballCoords
