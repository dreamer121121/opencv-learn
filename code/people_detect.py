import cv2
import numpy as np

def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih

def draw_person(image, person):
  x, y, w, h = person
  cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

img = cv2.imread("../images/people.jpg") #直接进行检测的图像。
hog = cv2.HOGDescriptor() #获取HOG描述子,总共为105*4*9+1维的特征向量。


hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#调用SVM分类器，利用HOG特征构建的SVM分类器已经被内置到opencv中


found, w = hog.detectMultiScale(img, winStride=(8,8),scale=1.05)


found_filtered = []
for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and is_inside(r, q):
            break
    else:
        found_filtered.append(r)

for person in found_filtered:
  draw_person(img, person)

cv2.imshow("people detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()