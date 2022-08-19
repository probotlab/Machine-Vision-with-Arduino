import cv2
import mediapipe as mp
import time
import controller as cmt

time.sleep(2.0)

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0) # cap = cv2.VideoCapture('http://101.101.1.101:1010/video') ...... for droidcam feed
cap.set(3, 1280)
cap.set(4, 720)
pTime = 0

with mp_hand.Hands(min_detection_confidence=0.7,
                   min_tracking_confidence=0.7) as hands:
 while True:
        success,image = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(image, f'FPS: {(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX,
                    2, (255, 8, 255), 2)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        ImList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, Im in enumerate(myHands.landmark):
                    h,w,c = image.shape
                    cx,cy = int(Im.x*w), int(Im.y*h)
                    ImList.append([id,cx,cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers = []
        if len(ImList) != 0:
            if ImList[tipIds[0]][1] > ImList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if ImList[tipIds[id]][2] < ImList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total = fingers.count(1)
            cmt.led(total)
            if total == 0:
                cv2.rectangle(image, (20, 300), (370, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FINGERS", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
            elif total == 1:
                cv2.rectangle(image, (20, 300), (370, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FINGERS", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
            elif total == 2:
                cv2.rectangle(image, (20, 300), (370, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FINGERS", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
            elif total == 3:
                cv2.rectangle(image, (20, 300), (370, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FINGERS", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
            elif total == 4:
                cv2.rectangle(image, (20, 300), (370, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FINGERS", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
            elif total == 5:
                cv2.rectangle(image, (20, 300), (370, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FINGERS", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)

        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
cv2.destroyAllWindows()
