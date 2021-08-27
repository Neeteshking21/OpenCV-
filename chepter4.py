# Chepter 4 Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[300:400, 100:300] = 255,0,0      # [start, end]
                    # width, hight
cv2.line(img, (0,0), (512, 512), (0, 255, 0), 1)  # (src, start, end, color, thickness)
cv2.rectangle(img, (0,200), (200, 400), (0,0,255), cv2.FILLED)   #(src, start, end, color, thickness)
cv2.circle(img, (400, 100), 100, (255,200,28), 2)       #(src, center, radious, color, thickness/cv2.FILLED)
cv2.putText(img, "Hello, Neetesh", (20,300), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 255, 80 ),2)  #(src, text, start, font, font_scale, color, thickness  )

cv2.imshow("Zeros", img )   

cv2.waitKey(0)