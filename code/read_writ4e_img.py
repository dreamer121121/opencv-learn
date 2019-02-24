import numpy as np
import cv2
# image = cv2.imread('learn.jpg')
# grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为二维数组
# print('----grayimage-----', grayimage.shape)
# print('----image----', image.shape)
# image[0, 0] = [255, 255, 255]
# cv2.namedWindow("Image")
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 读取灰度图像
image = cv2.imread('learn.jpg', 0)
cv2.namedWindow("Image")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img = np.zeros((4, 4), dtype=np.uint8)
# print('----img----', img)
# img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# print('----14----', img2)
# print('----img2.shape----', img2.shape)
# img2[0, 1] = [1, 1, 1]
# print('----17----', img2)
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
# image = cv2.imread('learn.jpg')
# grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为二维数组
# print(image.size)
# print(image.shape)
# cv2.namedWindow("Image")
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
