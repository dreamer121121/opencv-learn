import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, -8, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

img = cv2.imread(r'./images/learn.jpg', 0)  # 读取成灰度图像
k3 = ndimage.convolve(img, kernel_3x3)  # 返回的是做过卷积之后的图像
k5 = ndimage.convolve(img, kernel_5x5)
blurred = cv2.GaussianBlur(img, (11, 11), 0)  # 用高斯核卷原图像
g_hpf = img-blurred
cv2.imshow("img", img)
cv2.imshow("3X3", k3)
cv2.imshow("5X5", k5)
cv2.imshow("lpf", blurred)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()
