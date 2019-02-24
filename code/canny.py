import cv2
import numpy as np

# 读取原图像
img = cv2.imread(r"./images/statue_small.jpg")
cv2.imshow("initial_img", img)

# 转换为灰度图像
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_img", grayimg)

# 进行模糊处理（高斯滤波）
blurred = cv2.GaussianBlur(grayimg, (11, 11), 0)
cv2.imshow("blurred", blurred)

"""提取边缘特征并保存图像"""

# （1）用原始图像提取边缘特征
edges = cv2.Canny(grayimg, 200, 300)
cv2.imwrite("canny.jpg", edges)
cv2.imshow("canny", cv2.imread("canny.jpg"))

# （2）用高斯滤波后的图像提取边缘特征
edges_blurred = cv2.Canny(blurred, 200, 300)
cv2.imwrite("canny_blurred.jpg", edges_blurred)
cv2.imshow("canny_blurred", cv2.imread("canny_blurred.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
