#-*- coding: utf-8 -*-

# 打开摄像头并识别人脸

import cv2
import sys
from PIL import Image

def catchVideo(window_name, camera_id) :
    cv2.namedWindow(window_name)

    # 视频源
    cap = cv2.VideoCapture(camera_id)

    # 人脸识别分类器
    classfier = cv2.CascadeClassifier("/Users/denghb/Documents/py/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml")

    # 颜色(RGB)
    color = (0, 255, 0)

    while cap.isOpened() :
        ok, frame = cap.read() # 读取一帧
        if not ok:
            break # 读取失败
        
        # 将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0 :
            for faceRect in faceRects :
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x -10, y - 10), (x + w + 10, y + h + 10), color, 2)
        
        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q') :
            break
        
    # 释放摄像头
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    if len(sys.argv) != 2 :
        print(u"请执行：python %s 0 或 1 或 2" % (sys.argv[0]))
    else :
        catchVideo("face", int(sys.argv[1]))