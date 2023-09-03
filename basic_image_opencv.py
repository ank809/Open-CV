import cv2
# print(cv2.__version__)

# this imread function is used to read an image from the folder
img= cv2.imread('data from opencv/home.jpg', -1)

# if we print the image then the output we get will be in numeric form as in ML image is stored in form of numbers
print(img)

# imshow function is used to display an image

cv2.imshow('image',img )

# waitKey is used to show that how much time the image should be available on the screen
# if we pass delay as 0 then the image will not disappear until we cut the window
k=cv2.waitKey(0)

# this function is used to destroy all thw windows because if we don't do that then all the windows will be there
cv2.destroyAllWindows()

# if you want to write an image use imwrite() and in this you can give image name as anything you want
#cv2.imwrite('lena2.jpg', img)

# if you want to write the image by pressing a particular key
# k=cv2.waitKey(0)
print(k)
# as in ML everthing is in number, so we also have to change the q into its ASCII value
if k==ord('q'):
    cv2.imwrite('lena2.jpg', img)
elif k==ord('n'):
    img2= cv2.imread('data from opencv/lena.jpg')
    cv2.imshow('image2',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
