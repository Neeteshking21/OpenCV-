import cv2

# print("Package imported")


# Reading Images
# img = cv2.imread('src/dp.jpg')
#
# cv2.imshow('Our Output', img)
# cv2.waitKey(0)


#playing Video
"""
cap = cv2.VideoCapture('src/video.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         print("Stop")
        break
"""


# Playing video using webCam
# cap.set(ID, value)
cap = cv2.VideoCapture(0)

# change height
cap.set(3, 640)

#change width
cap.set(4, 640)

#change brightness
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow('WebCam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

