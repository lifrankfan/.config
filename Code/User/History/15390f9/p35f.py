import cv2
import mediapipe as mp
import numpy as np
import time
import HandDetection as hd

cam_width, cam_height = 640, 480
prev_time = 0

cap = cv2.VideoCapture(0)
cap.set(3, cam_width)
cap.set(4, cam_height)

detector = hd.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    landmarks = detector.findPosition(img)



    
    # fps
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()