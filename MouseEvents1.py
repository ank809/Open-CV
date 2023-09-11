import cv2
import numpy as np

event= [i for i in dir(cv2) if "EVENT" in i]

print(event)

def clickEvent(event, x , y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
        font= cv2.FONT_HERSHEY_PLAIN
        strCordinates= str(x) + " "+ str(y)
        cv2.putText(img, strCordinates, (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow("image", img)

    if event==cv2.EVENT_RBUTTONUP:
        blue= [y, x, 0]
        green= [y, x, 1]
        red= [y, x, 2]
        strColor= str(blue)+" "+ str(green)+" "+str(red)
        font= cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, strColor, (x, y), font , 1, (233, 45, 125), 2)
        cv2.imshow("image", img)

img= cv2.imread('data from opencv/lena.jpg', )
cv2.imshow("image", img)
cv2.setMouseCallback("image", clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()