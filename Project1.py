#vartual paint

import cv2
import numpy as np


cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

myColors = [
    [0, 77, 204, 20, 255, 255],
    [138, 62, 1, 161, 255, 255]
]

myColorVal = [
    [66,129,245],
    [194, 17, 247]
]

myPoints = []     # [x ,y, colorID]

def findcolor(img, myColors, myColorVal):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHsv, lower, upper)
        x, y = getContours(mask)
        # cv2.circle(imgCont, (x,y), 10, myColorVal[count], cv2.FILLED)
        if x!=0 and y!= 0:
            newPoints.append([x, y, count])
        count+=1
        # cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        x,y,w,h = 0,0,0,0
        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area>100:
                # cv2.drawContours(imgCont, cnt, -1, (255,0,0), 2)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x, y, w, h = cv2.boundingRect(approx)
        return x+w//2, y

def drawOnCanvas(myPoints, myColorVal):
    for point in myPoints:
        cv2.circle(imgCont, (point[0], point[1]), 10, myColorVal[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgCont = img.copy()
    cv2.imshow('camera', img)
    newPoints = findcolor(img, myColors, myColorVal)
    if len(newPoints)!= 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorVal)

    cv2.imshow('Result', imgCont)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

