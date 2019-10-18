import cv2
img = cv2.imread('../../images/learn.jpg')
horizontal = cv2.flip(img,1,dst=None)
cv2.imshow("img",img)
cv2.imshow("horizontal",horizontal)
k = cv2.waitKey(0)
