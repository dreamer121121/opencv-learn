import cv2
filename = "../../images/people.jpg"
def detect(filename):
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    #基于Harr特征的级联分类器。经典套路：特征(Harr特征，人工设计的特征)+机器学习(AdaBoost),在检测过程中依然采用滑动窗口技术。
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.namedWindow("face_detector")
    cv2.imshow("face_detector",img)
    cv2.imwrite('./result.jpg',img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
if __name__ == '__main__':
    detect(filename)
