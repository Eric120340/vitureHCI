# 这是一个示例 Python 脚本。
import cv2
import time
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)


# 按间距中的绿色按钮以运行脚本。


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
