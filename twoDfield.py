import cv2 as cv
import numpy as np
class Field:
    def __init__(self,info):
        self.info = info
    def makeAppField(self):
        field = np.zeros((self.info['height'] + self.info['pad']*2,self.info['width'] + self.info['pad']*2,3),np.uint8)
        return field
    def makepadding(self,field):
        #Creates field
        (xb1, yb1) = (self.info['pad'], self.info['pad'])
        (xb2, yb2) = (self.info['pad'] + self.info['width'], self.info['pad'])
        (xb3, yb3) = (self.info['pad'] + self.info['width'], self.info['pad'] + self.info['height'])
        (xb4, yb4) = (self.info['pad'], self.info['pad'] + self.info['height']) 
        (centerxtop,centerytop) = (int(round(self.info['width']/2,0) + self.info['pad']),self.info['height'] + self.info['pad'])
        (centerxbot,centerybot) = (int(round(self.info['width']/2,0) + self.info['pad']),self.info['pad'])
        #(goalboxx,goalboxy) = (self.info['pad'],int(round(self.info['height']*.75,0)))
        #(goalboxxout,goalboxyout) = (self.info['pad'] + 100 ,int(round(self.info['height']*.75,0)))
        coords = [(xb1, yb1), (xb2, yb2), (xb3, yb3), (xb4, yb4)]
        colors = (0,255,0)
        cv.line(field, coords[0], coords[1], colors, 2)
        cv.line(field, coords[2], coords[3], colors, 2)
        cv.line(field, coords[1], coords[2], colors, 2)
        cv.line(field, coords[3], coords[0], colors, 2)
        cv.line(field,(centerxtop,centerytop),(centerxbot,centerybot), colors, 2)
        ##cv.line(field,(goalboxx,goalboxy),(goalboxxout,goalboxyout), colors, 1)

        return field
    def addplayers(self,coords,field):
        ##Adds players to field object
        red = (0,0,255)
        for coord in coords['players']:
            ##field[int(coord[1]),int(coord[0])] = red
            field = cv.circle(field,(int(coord[0]),int(coord[1])),10,red,2)
        return field
        
    