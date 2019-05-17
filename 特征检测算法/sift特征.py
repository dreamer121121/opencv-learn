import cv2
import sys
import numpy as np

imgpath = sys.argv[1]
print('--impath--',imgpath)
img = cv2.imread(imgpath)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create() #实例化一个对象。
keypoints,descriptor = sift.detectAndCompute(gray,None)

img = cv2.drawKeypoints(image = img,outImage=img,keypoints=keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                        color=(51,163,236))
cv2.imwrite("sift_keypoints.jpg",img)
cv2.imshow('sift_keypoints',img)
while(True):
    if cv2.waitKey(int(1000 / 12)) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()