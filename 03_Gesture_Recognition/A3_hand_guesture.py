import cv2
import mediapipe as mp
import time
import math
import requests

host=input("Enter brain block ip address : ")


def hand_gestures():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    
    cooldown_time = 0  # Set the cooldown time in seconds
    last_detection_time = time.time()
    
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        h, w, c = img.shape
        results = hands.process(img)
        
        if not results.multi_hand_landmarks:
            requests.get(f"http://{host}/?cmd=s")
            print("STOPPED")
    
        elif results.multi_hand_landmarks:
            current_time = time.time()
            elapsed_time_since_last_detection = current_time - last_detection_time
    
            if elapsed_time_since_last_detection > cooldown_time:
                for hand_idx, hand_landmark in enumerate(results.multi_hand_landmarks):
                    lm_list = [lm for lm in hand_landmark.landmark]
                    finger_fold_status = [lm_list[tip].y < lm_list[tip - 2].y for tip in finger_tips]
                    print(finger_fold_status)
    
                    if not any(finger_fold_status):  # All fingers closed
                        cv2.putText(img, "RUN", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                        print("RUN")
                        requests.get(f"http://{host}/?cmd=f")
                        last_detection_time = time.time()  # Update the last detection time
    
                    if all(finger_fold_status):  # All fingers open
                        cv2.putText(img, "STOP", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                        print("STOP")
                        requests.get(f"http://{host}/?cmd=s")
                        last_detection_time = time.time()  # Update the last detection time
    
                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            thumb_tip = hand_landmarks.landmark[4]
                            palm_base = hand_landmarks.landmark[0]
    
                            thumb_direction_vector = (thumb_tip.x - palm_base.x, thumb_tip.y - palm_base.y)
    
                            thumb_direction_angle_degrees = math.degrees(math.atan2(thumb_direction_vector[1], thumb_direction_vector[0]))
                            print(thumb_direction_angle_degrees)
    
                            if finger_fold_status[0]:  # Thumb extended to Right, other fingers closed
                                if not any(finger_fold_status[1:]) and -56 <= thumb_direction_angle_degrees <= 0:
                                    cv2.putText(img, "LEFT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                                    print("LEFT")
                                    requests.get(f"http://{host}/?cmd=l")
                                    last_detection_time = time.time()
    
                                if any(finger_fold_status[1:]):
                                    requests.get(f"http://{host}/?cmd=s")
                                    last_detection_time = time.time()
    
                                if not any(finger_fold_status[1:]) and -180 <= thumb_direction_angle_degrees <= -120:
                                    cv2.putText(img, "RIGHT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                                    print("RIGHT")
                                    requests.get(f"http://{host}/?cmd=r")
                                    last_detection_time = time.time()
                                    
                            else:
                                print("Thumb Direction: Undefined")
                    
                    if any(finger_fold_status) and not all(finger_fold_status) and not finger_fold_status[0]:
                        requests.get(f"http://{host}/?cmd=s")
                        last_detection_time = time.time()
    
                    cv2.arrowedLine(img, (int(palm_base.x * img.shape[1]), int(palm_base.y * img.shape[0])),
                                (int(thumb_tip.x * img.shape[1]), int(thumb_tip.y * img.shape[0])),
                                (0, 255, 0) if 0 <= thumb_direction_angle_degrees <= -56 else
                                (255, 0, 0) if -180 <= thumb_direction_angle_degrees <= -120 else
                                (0, 0, 255), 2)
                                    
                    mp_draw.draw_landmarks(img, hand_landmark,
                                        mp_hands.HAND_CONNECTIONS,
                                        mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                        mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                        )
        
        cv2.imshow("Hand Sign Detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            requests.get(f"http://{host}/?cmd=s")
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == '__main__':
    hand_gestures()
