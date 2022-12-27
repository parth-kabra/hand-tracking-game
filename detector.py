import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
from objects import setJson

detector=HandDetector(
    detectionCon=0.8,
    maxHands=1
)

video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):

    ret, frame = video.read()
    hand, img= detector.findHands(frame, draw=True)

    if (hand):

        fingers=hand[0]
        fingerUp=detector.fingersUp(fingers)

        setJson({
            "handCount":fingerUp,
            "hand":True   
        })

        fingerCount = fingerUp.count(1)

        if(fingerCount == 0):
            keyboard.press_and_release("space")

    else:
        setJson({
            "hand":False
        })

    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()