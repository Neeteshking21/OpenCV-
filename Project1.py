#vartual paint

import cv2
import numpy as np


cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

myColors = [
    [0, 77, 204, 20, 255, 255],
    [149, 56, 120, 169, 254, 255]
]

def findcolor(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHsv, lower, upper)
        cv2.imshow(str(color[0]), mask)

while True:
    success, img = cap.read()
    cv2.imshow('camera', img)
    findcolor(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

