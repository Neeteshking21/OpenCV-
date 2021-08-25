# Basic functions

import cv2
import numpy as np
img = cv2.imread('src/dp.jpg' )

kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3,3), 4)
imgcanny = cv2.Canny(img, 70, 70)
imgDilation = cv2.dilate(imgcanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny', imgcanny)
cv2.imshow('Dilation', imgDilation)
cv2.imshow('Erode images', imgEroded)
cv2.waitKey(0)

