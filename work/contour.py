import cv2 as cv 
import numpy as np

image = cv.imread("../../footage/gameimg.jpg")
new_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(new_image,127,255,0)
contours,hierarchy = cv.findContours(thresh,2,1)
cont = contours[0]

rect = cv.minAreaRect(cont)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(image,[box],0,(0,0,255),2)
cv.imshow("Nmin",image)
cv.imshow("new",new_image)
