import cv2 as c

img= c.imread('data from opencv/lena.jpg')
img1= c.imread('data from opencv/messi5.jpg')

print(img.size)
print(img.shape)
print(img.dtype)

#  if you want to change an image
b, g, r= c.split(img)
print(b)
print(g)
print(r)

#  it changes all the pixels from previous to a new image
# img1= c.merge((b, g, r))

#  if you want to copy a particular part of area of the image  and paste it in other location
ball = img1[280:340, 330:390]
#
# This line extracts a region of interest (ROI) from the img image.
# The ROI is defined by a specific rectangular area specified by coordinates.
# The format is img[y1:y2, x1:x2], where (y1, x1) represents the top-left corner and (y2, x2) represents the bottom-right corner of the rectangular region.
# In this case, img[280:340, 330:390] selects a rectangular region from (280, 330) to (339, 389) in the img image. This rectangular region is essentially a portion of the image, and it is assigned to the variable ball.
# img[273:333, 100:160] = ball:
#
# This line replaces another rectangular region in the img image with the content stored in the ball variable.
# Similar to the previous line, it defines a rectangular region with coordinates (273, 100) as the top-left corner and (332, 159) as the bottom-right corner.
# The content of the ball variable (the region previously extracted from the image) is then assigned to this rectangular region in img.
img1[273:333, 100:160]= ball

#  if you want to resize an image
img1= c.resize(img1, (512, 512))

c.imshow('image1', img1)
c.waitKey(0)
c.destroyAllWindows()