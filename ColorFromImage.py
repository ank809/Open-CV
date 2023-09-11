import cv2
import numpy as np

img= cv2.imread('data from opencv/home.jpg')
cv2.imshow("image", img)

events= [i for i in dir(cv2) if 'EVENT' in i]

def clickMouse(events, x, y ,flags, param):
    if events== cv2.EVENT_LBUTTONDOWN:
        blue= img[y, x, 0]
        green= img[y, x, 1]
        red= img[y, x, 2]
        colorImage= np.zeros((536, 536, 3), np.uint8)
        colorImage[:]= [blue, green, red]
        cv2.imshow("image1", colorImage)

cv2.setMouseCallback("image", clickMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()