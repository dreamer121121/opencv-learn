import cv2
import numpy as np
import os


def save_img():
    video_path = r'C:\Users\dreamer\Desktop\opencv-learn\videos'
    videos = os.listdir(video_path)
    for video_name in videos:  # 逐个视频进行截取
        file_name = video_name.split('.')[0]
        folder_name = file_name
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path + '\\'+video_name)  # 读入视频文件
        # print('----total frame num ----', vc.get(7))
        # print('-----fps------:',vc.get(5))
        c = 1  # 记录帧数
        if vc.isOpened():  # 判断是否正常打开
            rval, frame = vc.read()  # 自动读取下一帧
        else:
            rval = False
        timeF = 50  # 视频帧计数间隔频率

        while rval:  # 循环读取视频帧
            print('----current frame----', c)
            rval, frame = vc.read()
            pic_path = folder_name + '/'  # 指定图片存入的路径相当于起到了os.chdir()的作用。
            if (c % timeF == 0):  # 每隔timeF帧进行存储操作
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储图像且能够自动覆盖之前的同名文件
            c = c + 1
            cv2.waitKey(1)
        vc.release()


if __name__ == '__main__':
    save_img()
