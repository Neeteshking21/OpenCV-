# Joining Images

import cv2
import numpy as np

img = cv2.imread('src/dp.jpg')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow('Image Joining Horigentel', imgHor)
cv2.imshow('Image Joining Vertical', imgVer)
cv2.waitKey(0)