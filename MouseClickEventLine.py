import cv2;
import numpy as np

img= np.zeros((556, 556, 3), np.uint8)
events= [i for i in dir(cv2) if "EVENT" in i]
print(events)

def clickMouseEvent(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (255, 34, 126), 3)
        points.append((x, y))
        if(len(points)>=2):
            cv2.line(img, points[-1], points[-2], (234, 235, 255), 4)
        #     here we are using -1 and -2 because we only need last 2 points
        cv2.imshow("image", img)

cv2.imshow("image", img)
points=[]
cv2.setMouseCallback("image", clickMouseEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()