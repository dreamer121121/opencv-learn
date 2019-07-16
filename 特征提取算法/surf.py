import cv2
import sys
import numpy as np

imgpath = sys.argv[1]
img = cv2.imread(imgpath)
alg = sys.argv[2] #指定使用的是哪一个特征检测算法

def fd(algorithm):
    if algorithm == 'SIFT':
        return cv2.xfeatures2d.SIFT_create() #实例化sift对象
    else:
        return cv2.xfeatures2d.SURF_create(float(sys.argv[3]) if len(sys.argv) == 4 else 4000)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create() #实例化一个对象。
keypoints,descriptor = sift.detectAndCompute(gray,None) #进行检测和计算特征点描述子


img = cv2.drawKeypoints(image = img,outImage=img,keypoints=keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                        color=(51,163,236))

cv2.imwrite("sift_keypoints.jpg",img)
cv2.imshow('sift_keypoints',img)

while(True):
    if cv2.waitKey(int(1000 / 12)) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()
