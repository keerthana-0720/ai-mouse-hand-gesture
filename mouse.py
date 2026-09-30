import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)

hand = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand.process(rgb)

    hands = output.multi_hand_landmarks

    h, w, _ = frame.shape

    if hands:
        for i in hands:

            draw.draw_landmarks(
                frame,
                i,
                mp.solutions.hands.HAND_CONNECTIONS
            )

            for id, lm in enumerate(i.landmark):

                x = int(lm.x * w)
                y = int(lm.y * h)

                if id == 8:
                    cv2.circle(frame, (x,y), 10, (0,255,0), -1)

                    mouse_x = screen_w / w * x
                    mouse_y = screen_h / h * y

                    pyautogui.moveTo(mouse_x, mouse_y)

    cv2.imshow("AI Mouse", frame)

    if cv2.waitKey(1) == 27:
        break