import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
from time import sleep
import time
import pyfirmata

comport = 'COM5'

board = pyfirmata.Arduino(comport)

enA1 = board.get_pin('d:6:o')
in11 = board.get_pin('d:4:o')
in12 = board.get_pin('d:3:o')
in13 = board.get_pin('d:2:o')
in14 = board.get_pin('d:13:o')
enB1 = board.get_pin('d:5:o')
enA2 = board.get_pin('d:10:o')
in21 = board.get_pin('d:12:o')
in22 = board.get_pin('d:11:o')
in23 = board.get_pin('d:8:o')
in24 = board.get_pin('d:7:o')
enB2 = board.get_pin('d:9:o')

# cap = cv2.VideoCapture('http://localhost:xyxy/mjpegfeed') ... through usb droidcam
# cap = cv2.VideoCapture('http://xyz.xyz.x.xyz:xyxy/video') .. for droidcam feed
cap = cv2.VideoCapture(2)
cap.set(3, 1280)
cap.set(4, 720)
pTime = 0

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Find Function
# x is the raw distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

# Loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 0)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40,70), cv2.FONT_HERSHEY_COMPLEX,
                2, (255, 8, 255), 2)

    hands = detector.findHands(img, draw=False)

    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        x1, y1, z1 = lmList[5]
        x2, y2, z2 = lmList[17]
        # print(x1)
        # 0 - 640
        distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
        A, B, C = coff
        distanceCM = int(A * distance ** 2 + B * distance + C)

        print(distanceCM)

        if x1<426:
            print("right")
            enA1.write(1)
            in11.write(0)
            in12.write(0)
            in13.write(1)
            in14.write(1)
            enB1.write(1)
            enA2.write(1)
            in21.write(1)
            in22.write(0)
            in23.write(0)
            in24.write(1)
            enB2.write(1)


        elif x1>=426 and x1<852:
            if distanceCM<65:
                print("backward")
                enA1.write(1)
                in11.write(0)
                in12.write(1)
                in13.write(1)
                in14.write(0)
                enB1.write(1)
                enA2.write(1)
                in21.write(0)
                in22.write(1)
                in23.write(0)
                in24.write(1)
                enB2.write(1)

            else:
                print("forward")
                enA1.write(1)
                in11.write(1)
                in12.write(0)
                in13.write(0)
                in14.write(1)
                enB1.write(1)
                enA2.write(1)
                in21.write(1)
                in22.write(0)
                in23.write(1)
                in24.write(0)
                enB2.write(1)

        else:
            print("left")
            enA1.write(1)
            in11.write(1)
            in12.write(1)
            in13.write(0)
            in14.write(0)
            enB1.write(1)
            enA2.write(1)
            in21.write(0)
            in22.write(1)
            in23.write(1)
            in24.write(0)
            enB2.write(1)


        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        #cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))

    else:
        print("No hand Detected!")
        enA1.write(0)
        in11.write(0)
        in12.write(0)
        in13.write(0)
        in14.write(0)
        enB1.write(0)
        enA2.write(0)
        in21.write(0)
        in22.write(0)
        in23.write(0)
        in24.write(0)
        enB2.write(0)


    # cv2.flip(cv2.imshow("Image", img), 0)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
