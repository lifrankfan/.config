import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,
                 mode=False,
                 max_hands=2,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, 
                                         self.max_hands, 
                                         self.min_detection_confidence, 
                                         self.min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

def findHands(self, img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = self.hands.process(imgRGB)

    #  iterate through hands and display them
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, landmark in enumerate(hand_landmarks.landmark):
                # print(id, landmark)
                # convert decimal to pixel
                h, w, c = img.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 25, (255, 0, 255), cv2.FILLED)

            self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)


def main():
    prev_time = 0
    curr_time = 0
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        # calculate fps
        curr_time = time.time()
        fps = 1/(curr_time-prev_time)
        prev_time = curr_time
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()