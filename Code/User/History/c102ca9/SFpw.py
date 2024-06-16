import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()

# import cv2
# import mediapipe as mp
# import time

# class handDetector():
#     def __init__(self,
#                  mode=False,
#                  max_hands=2,
#                  min_detection_confidence=0.5,
#                  min_tracking_confidence=0.5):
#         self.mode = mode
#         self.max_hands = max_hands
#         self.min_detection_confidence = min_detection_confidence
#         self.min_tracking_confidence = min_tracking_confidence

#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands(self.mode, 
#                                          self.max_hands, 
#                                          self.min_detection_confidence, 
#                                          self.min_tracking_confidence)
#         self.mp_draw = mp.solutions.drawing_utils

#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(imgRGB)

#         #  iterate through hands and display them
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 if draw:
#                     self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        
#         return img

#                 # for id, landmark in enumerate(hand_landmarks.landmark):
#                 #     # print(id, landmark)
#                 #     # convert decimal to pixel
#                 #     h, w, c = img.shape
#                 #     cx, cy = int(landmark.x*w), int(landmark.y*h)
#                 #     print(id, cx, cy)
#                 #     if id == 0:
#                 #         cv2.circle(img, (cx,cy), 25, (255, 0, 255), cv2.FILLED)



# def main():
#     prev_time = 0
#     curr_time = 0
#     cap = cv2.VideoCapture(0)
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         # calculate fps
#         curr_time = time.time()
#         fps = 1/(curr_time-prev_time)
#         prev_time = curr_time
#         cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
#         cv2.imshow("Image", img)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break


# if __name__ == "__main__":
#     main()