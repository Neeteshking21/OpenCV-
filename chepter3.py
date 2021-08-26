# Chepter 3 Resizing and Cropping

import cv2
import numpy as np

img = cv2.imread('src/dp.jpg')
print(img.shape)

imgResize = cv2.resize(img, (900, 800))
imgCrop = img[:200, 500:]

cv2.imshow('Original Imgae', img)
cv2.imshow('Resize Image', imgResize)
cv2.imshow('Cropped Image', imgCrop)
cv2.waitKey(0)