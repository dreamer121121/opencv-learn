from Basic_Class import *
import cv2
import numpy as np

img = cv2.imread(r"../reverse_cars.jpg", 0)
cv2.imshow("img", img)

# 进行gamma变换
img = gamma_trans(img, 5)
cv2.imshow("gamma", img)
cv2.waitKey()
cv2.destroyAllWindows()
