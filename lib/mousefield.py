import cv2 as cv 
import numpy as np
#Gets field information from user, and edits the field of view to Top down
#####################
def totalpic(points):
    heigths = [i[0] for i in points]
    widths = [i[1] for i in points] 
    result_h = max(heigths) - min(heigths)
    result_w = max(widths) - min(widths)
    return result_h,result_w

def mouseGet(video):
    points = []
    def mousedraw(event,x,y,flags,params):
        ##coords = {'topRight':0,"topLeft":0,"bottomRight":0,"bottomLeft":0}
        if event == cv.EVENT_LBUTTONDBLCLK:
            points.append((x,y))
    while True:
        cv.namedWindow('Frame')
        cv.setMouseCallback('Frame',mousedraw)
        while True:
            ret,frame = video.read()
            print(len(points))
            cv.imshow("Frame",frame)
            key = cv.waitKey(0)
            if key == ord('q'):
                break
        if len(points) == 4:
            break
    video.release()
    cv.destroyAllWindows()
    height, width = totalpic(points)
    return height,width,points
