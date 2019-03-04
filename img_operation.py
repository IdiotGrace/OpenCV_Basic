import cv2 as cv
import numpy as np


# imread can define the mode of loading image, default mode is RGB
colorImage = cv.imread('img/pic4.jpg', cv.IMREAD_COLOR)
# the parameter can be chonsen: CV_IMREAD_COLOR(RGB), CV_IMREAD_GRAYSCALE(grayscale), CV_IMREAD_UNCHANGED(neither)
cv.namedWindow("colorImage", cv.WINDOW_AUTOSIZE)
cv.imshow("colorImage", colorImage)
k = cv.waitKey(0)
if k == 27:   # wait for ESC key to exit
	cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
	cv.imwrite('pic4color.png', colorImage)
	cv.destroyAllWindows()



# get properties of image
img = cv.imread('img/pic4.jpg')
print(img.shape) # 行数，列数， 通道数； 行数，列数
print(img.size)
print(img.dtype)


img = cv.imread('img/pic4.jpg')
px = img[100, 100] #return the value of B, G, R
print(px)
blue = img[100, 100, 0]
print(blue)

# modify pixel value
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# Numpy: array.item(), array.itemset()
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

'''
part = img[10:90, 30:110]
cv.imshow("partImage", part)
'''

# split and merge channels
b, g, r = cv.split(img)
cv.imshow("b", b)
k = cv.waitKey(0)
if k == 27:   # wait for ESC key to exit
	cv.destroyAllWindows()













