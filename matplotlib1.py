import cv2
from matplotlib import pyplot as plt

img= cv2.imread('data from opencv/sudoku.png', 0)

_, th1= cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

#  it will do the reverse of above
_, th2= cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)

# till the thresh the value of pixels will not change, after it will remain as thresh
_, th3= cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)

# when pixel is lesser than thresh, the pixel assign is 0, and when it it greater than
# 50(thresh) , it will remain same
_, th4= cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)

# it is a vice versa of above
_, th5= cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)

titles= ["Images", "Binary", "Binary_Inv", "TRUNC", "TOZERO", "TOZERO_INV"]
images= [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    # plt.xticks([])
    plt.yticks([])
#     xticks and yticks are used to remove the points in both on x and y axis

plt.show()

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()