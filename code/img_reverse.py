import cv2
import numpy as np

# 读取图像
img = cv2.imread(r'./images/cars.jpg',0)
cv2.imshow("img", img)
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimg", grayimg)
img[:, :] = 255 - img[:, :]
cv2.imshow("reverse", img)
cv2.imwrite("reverse_cars.jpg", img)

# 图像取反
cv2.waitKey()
cv2.destroyAllWindows()


