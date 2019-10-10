import cv2
import numpy as np
"""
若Sobel算子的kenel大小为3则在进行导数运算时同时进行了高斯滤波。若ksize=1则只会进行求导运算与书上的计算公式相同。
"""
img = cv2.imread("../images/learn.jpg")
cv2.imshow("img",img)
resultx = cv2.Sobel(img,-1,1,0) #若ksize=-1则必须保证dx+dy==1
cv2.imshow("resusltx",resultx)
resulty = cv2.Sobel(img,-1,0,1)
cv2.imshow("resulty",resulty)
sobley = cv2.convertScaleAbs(resulty) #像素取绝对值convertScaleAbs()
sobelx = cv2.convertScaleAbs(resultx)
# result = np.sqrt(sobley**2+sobelx**2).astype(int)
# print(result)
#简化为Gx+Gy
result = cv2.addWeighted(sobelx,0.5,sobley,0.5,0)
one_step = cv2.Sobel(img,-1,1,1)
one_step = cv2.convertScaleAbs(one_step)
cv2.imshow("one-step",one_step)
cv2.imshow("result",result)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
# cv2.Sobel()
