import cv2 as cv
import numpy as np;


def main(video):
    while True:
        ret,frame = video.read()
        if frame is None:
            print("Frame is None")
            break
        key = cv.waitKey(10)
        img_keys = blober(frame)
        cv.imshow("Src",frame)
        cv.imshow("Blob",img_keys)
        if key == ord('q') or key == 27:
            break
    video.release()
    cv.destroyAllWindows()

def blober(frame):
    params = cv.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 1500
    params.filterByCircularity = True
    params.minCircularity = 0.1
    params.filterByConvexity = True
    params.minConvexity = 0.87
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    detector = cv.SimpleBlobDetector_create(params)
    keypoints = detector.detect(frame)
    img_keys = cv.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_keys

if __name__ == "__main__":
    video = cv.VideoCapture(r"../footage/longgame.mp4")
    main(video)
