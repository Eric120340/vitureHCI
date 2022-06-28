import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

tipIds = [4, 8, 12, 16, 20]

detector = htm.handDetector(detectionCon=0.75)
while True:
    sccuess, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList[8])


    if len(lmList) != 0:
        fingers = []
        for id in range(0, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

    cv2.imshow("FingerCount", img)
    cv2.waitKey(1)