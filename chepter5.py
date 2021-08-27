# Warp perspective

import cv2
import numpy as np

img = cv2.imread('src/dp.jpg')

height, width = 960, 960

pts1 = np.float32([[111, 219],[287, 188], [154, 482], [352, 440]])
print(pts1)
pts2 = np.float32([[0, 0], [width, 0],[0, height], [width, height]])
print(pts2)
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imageout = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Warp image', imageout)
cv2.waitKey(0)