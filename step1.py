#-*- coding: utf-8 -*-

# 打开摄像头

import cv2
import sys
from PIL import Image

def catchVideo(window_name, camera_id):
    cv2.namedWindow(window_name)

    # 视频源
    cap = cv2.VideoCapture(camera_id)

    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        
        # 显示视频
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("UsageL%s camera_id\r\n" % (sys.argv[0]))
    else:
        catchVideo(u"截取视频流", int(sys.argv[1]))  

