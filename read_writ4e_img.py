import numpy as np
import cv2

image = cv2.imread('learn.jpg')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为二维数组
print('----grayimage-----', grayimage.shape)
print('----image----', image.shape)
image[0, 0] = [255, 255, 255]
cv2.namedWindow("Image")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
