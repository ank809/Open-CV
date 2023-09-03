# for working with videos
import cv2

cap= cv2.VideoCapture(0)
# cap= cv2.VideoCapture('data from opencv/Megamind.avi')
print(cap)

# for writing a video foucc is four color code
fourcc= cv2.VideoWriter.fourcc(*'XVID')
print(fourcc)
out= cv2.VideoWriter('video1.avi', fourcc, 20.0, (720, 528))

 # SUPPOSE IF YOU GAVE WRONG FILE NAME OF A VIDEO NAME THAT DO NOT EXIST THEN

print(cap.isOpened())
#  then in this case it will be false and you won't get any error
while(cap.isOpened()):
    # here we use tuple comprehension
    ret, frame= cap.read()

    #  if you want to get the height and width of the frames
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out.write(frame)

    # for changing the color of frames to grey
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video1', gray)

    # cv2.imshow('video', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
