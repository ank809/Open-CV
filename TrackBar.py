import cv2
import numpy as np
img = np.zeros((536, 536, 3), np.uint8)
cv2.namedWindow("image")

def do_nothing(x):
    print(x)

cv2.createTrackbar("B", "image", 0, 255, do_nothing)
cv2.createTrackbar("G", "image", 0, 255, do_nothing)
cv2.createTrackbar("R", "image", 0, 255, do_nothing)
switch= "0/1 , on/off"
cv2.createTrackbar(switch, "image", 0, 1, do_nothing)
while(1):
    cv2.imshow("image", img)
    k= cv2.waitKey(1)
    if k == 27 :
        break
    b= cv2.getTrackbarPos("B", "image")
    g = cv2.getTrackbarPos("G", "image")
    r= cv2.getTrackbarPos("R", "image")
    s= cv2.getTrackbarPos(switch, "image")

    if s==0:
        img[:]=0
    else:
        img[:]= [b, g, r]

cv2.destroyAllWindows()

#  255, 124, 140