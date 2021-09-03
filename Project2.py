# document scanner

import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 450)
cap.set(4, 600)
cap.set(10, 110)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5),1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)

    return imgThres

   def getContours(img):
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            print(area)
            if area>5000:
                cv2.drawContours(imgCont, cnt, -1, (255,0,0), 2)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    imgThres = preProcessing(img)
    imgCont = img.copy()
    cv2.imshow("Camera", img)
    cv2.imshow("imgThres", imgThres)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break