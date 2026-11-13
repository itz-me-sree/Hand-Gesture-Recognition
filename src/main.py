import cv2
from collections import Counter

from .hand_detector import HandDetector
from .gesture_recognizer import (
    LANDMARKS,
    is_thumb_open,
    is_finger_open,
    get_thumb_direction,
    identify_gesture
)


HISTORY_LENGTH = 5


def main():

    detector = HandDetector()
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        print("Error: Unable to open webcam.")
        detector.close()
        return

    gesture_history = []

    try:

        while True:

            success, img = video.read()

            if not success:
                print("Error: Unable to read webcam frame.")
                break

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = detector.process(img_rgb)

            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:

                    landmarks = hand_landmarks.landmark

                    finger_state = {

                        "THUMB": is_thumb_open(landmarks),

                        "INDEX": is_finger_open(
                            landmarks[LANDMARKS["INDEX_MCP"]],
                            landmarks[LANDMARKS["INDEX_PIP"]],
                            landmarks[LANDMARKS["INDEX_DIP"]]
                        ),

                        "MIDDLE": is_finger_open(
                            landmarks[LANDMARKS["MIDDLE_MCP"]],
                            landmarks[LANDMARKS["MIDDLE_PIP"]],
                            landmarks[LANDMARKS["MIDDLE_DIP"]]
                        ),

                        "RING": is_finger_open(
                            landmarks[LANDMARKS["RING_MCP"]],
                            landmarks[LANDMARKS["RING_PIP"]],
                            landmarks[LANDMARKS["RING_DIP"]]
                        ),

                        "LITTLE": is_finger_open(
                            landmarks[LANDMARKS["LITTLE_MCP"]],
                            landmarks[LANDMARKS["LITTLE_PIP"]],
                            landmarks[LANDMARKS["LITTLE_DIP"]]
                        )
                    }

                    thumb_direction = get_thumb_direction(landmarks)

                    gesture = identify_gesture(
                        finger_state,
                        thumb_direction
                    )

                    gesture_history.append(gesture)

                    if len(gesture_history) > HISTORY_LENGTH:
                        gesture_history.pop(0)

                    stable_gesture = Counter(
                        gesture_history
                    ).most_common(1)[0][0]

                    cv2.putText(
                        img,
                        stable_gesture,
                        (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.5,
                        (0, 0, 255),
                        3
                    )

                    detector.draw_landmarks(
                        img,
                        hand_landmarks
                    )

            else:
                gesture_history.clear()

            cv2.imshow("Gesture Recognition", img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        video.release()
        detector.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()