import cv2
import numpy as np
events= [i for i in dir(cv2) if 'EVENT' in i]

print(events)

img = cv2.imread('data from opencv/lena.jpg')

def ClickEvent(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)
        font= cv2.FONT_HERSHEY_PLAIN
        strCor= str(x) + " "+ str(y);
        cv2.putText(img, strCor, (x, y), font,1, (255, 34, 56), 2 )
        cv2.imshow('image', img)
    if events== cv2.EVENT_RBUTTONUP:
        blue= img[y, x, 0]
        green= img[y, x, 1]
        red= img[y, x, 2]
        font= cv2.FONT_HERSHEY_PLAIN
        strBGR= str(blue)+" "+ str(green) +" " +str(red)
        cv2.putText(img, strBGR, (x, y), font , 1, (34, 56, 234), 2)
        cv2.imshow("image", img)

cv2.imshow("image", img)
cv2.setMouseCallback("image", ClickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()


