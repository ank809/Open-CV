import cv2
import datetime

cap= cv2.VideoCapture('data from opencv/Megamind.avi')

while cap.isOpened():
     access, frames= cap.read()
     if access==True:
         font= cv2.FONT_HERSHEY_PLAIN
         text=str(datetime.datetime.now())
         frames= cv2.putText(frames, text, (10, 50), font, 1, (12, 233, 23),2 )
         cv2.imshow('video', frames)

         if cv2.waitKey(1)== ord('q'):
             break
     else:
             break
cap.release()
cv2.destroyAllWindows()