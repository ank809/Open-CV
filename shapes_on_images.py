import numpy as np

import cv2
img= cv2.imread('data from opencv/left05.jpg')
img= cv2.line(img, (0, 0), (255, 255), (0, 123, 78), 10)
img= cv2.arrowedLine(img, (10, 0), (245, 100), (0, 255 , 0), 8)
img= cv2.rectangle(img, (245, 34), (34, 356), (0, 13, 255), 5)

# if we give thickness as -1 then it will fill the color inside the shape

img= cv2.circle(img, (123, 133), 89, (12, 34, 63), -1)

# put text in an image
font= cv2.FONT_HERSHEY_COMPLEX
img= cv2.putText(img, 'Hello JimCorbett', (10, 250), font, 2, (122, 34, 156), 8)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()