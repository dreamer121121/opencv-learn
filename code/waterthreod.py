import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *#numpy+pyplot
img = cv2.imread("../images/basil.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("binary",thresh)

#为图像设置阈值,此处使用OTSU算法自动寻找合适的阈值(注意若使用此算法第二个参数threshold必须设为0)，ret即为返回的阈值
#
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)#进行一次开运算。
cv2.imshow("opening",opening)
k = cv2.waitKey(0)

# sure_bg = cv2.dilate(opening,kernel,iterations=3)#再一次进行膨胀运算。
# dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
# ret1,sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# sure_fg = np.uint8(sure_fg)
# unknown = cv2.subtract(sure_bg,sure_fg)
# ret2,markers = cv2.connectedComponents(sure_fg)
# markers += 1
# markers[unknown==255] = 0

# #打开门将水灌进来
# markers = cv2.watershed(img,markers)
# img[markers==-1] = [255,0,0]
# plt.imshow(img)
# plt.show()









