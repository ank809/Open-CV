import cv2
import numpy as np

#  create a black image
img1= np.zeros((255, 500, 3), np.uint8 )
img1= cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2= np.ones((255, 500, 3), np.uint8)
img2= cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)
img2= img2*255

# cv2.imshow('image 1', img1)
# cv2.imshow("image 2", img2)

bitand= cv2.bitwise_and(img1, img2)
bitor= cv2.bitwise_or(img1, img2)
bitxor = cv2.bitwise_xor(img1, img2)
bitnot1= cv2.bitwise_not(img1)
bitnot2= cv2.bitwise_not(img2)

# cv2.imshow('bitwiseAnd', bitand)
# cv2.imshow('bitwiseor', bitor)
# cv2.imshow('bitwisenot1', bitnot1)
# cv2.imshow('bitwisenot2', bitnot2)
# cv2.imshow('bitwisexor', bitxor)

img= cv2.imread('data from opencv/home.jpg', -1)

cv2.waitKey(0)
cv2.destroyAllWindows()