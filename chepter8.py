import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgCont, cnt, -1, (255,0,0), 2)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            print(x,y,w,h)
            if objCor == 3:
                objType = 'tri'
            elif objCor == 4 :
                aspRat = w/float(h)
                if aspRat>0.95 and aspRat < 1.05: objType = 'square'
                else: objType='Rectangle'

            else: objType='None'
            cv2.rectangle(imgCont, (x,y), (x+w, y+h), (0,255,0),2)
            cv2.putText(imgCont,objType,(x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))



img = cv2.imread('src/shapes.jpg')
imgCont = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7,7),1)
imgCan = cv2.Canny(img, 50, 50)

getContours(imgCan)

cv2.imshow('Original', img)
cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCan)
cv2.imshow('Contours', imgCont)

cv2.waitKey(0)