import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread('data from opencv/smarties.png', 0)

_, mask= cv2.threshold(img, 220, 255, cv2.THRESH_BINARY, )
kernal = np.zeros((2, 2), np.uint8)

dilation= cv2.dilate(mask, kernal, iterations=4)
erosion= cv2.erode(mask, kernal, iterations=4)
opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing= cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
gradient= cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
bh= cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernal)

titles= ["image", "mask", "dilation", "erosion", "opening", "closing", "gradient", "blackhat"]
images= [img, mask, dilation, erosion, opening, closing, gradient, bh]

for i in range(8):
    plt.subplots(3, 3,i+1),
    plt.imshow(images[i], cmap="gray")
    plt.title[titles[i]]
    plt.xticks()
    plt.yticks()

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
