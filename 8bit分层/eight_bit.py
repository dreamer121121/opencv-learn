import cv2
import numpy as np
from Basic_Class import *

img = cv2.imread('initial.tif', 0)
cv2.imshow('initial', img)
image = img.tolist()

i = 1
while i <= 8:
    array = []
    for each_row in image:
        temp = []
        for each_pixel in each_row:
            erjinzhi = '{:08b}'.format(each_pixel)
            if erjinzhi[-i] == '1':
                L = 255
            else:
                L = 0
            temp.append(L)
        array.append(temp)
    array = np.array(array, dtype=np.uint8)  # 此处若不指明数据类型会报错
    cv2.imshow(str(i)+'th', array)
    i += 1
    cv2.imwrite(str(i)+'th.jpg', array)

cv2.waitKey()
cv2.destroyAllWindows()
