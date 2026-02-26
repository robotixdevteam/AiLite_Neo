import cv2
import mediapipe as mp
import numpy as np
import requests
import warnings
warnings.filterwarnings("ignore")

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
host=input("Enter brain block ip address : ")

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

def classify_head_position(nose_tip, image_width, image_height):
    # Determine the position of the nose tip relative to the frame's center
    frame_center = np.array([image_width / 2, image_height / 2])
    direction_vector = nose_tip - frame_center

    # Threshold for considering the nose tip to be in the center
    center_threshold_x = image_width * 0.05  # Adjust as needed
    center_threshold_y = image_height * 0.05  # Adjust as needed

    # Compare the nose tip position to the frame's center
    if abs(direction_vector[0]) < center_threshold_x and abs(direction_vector[1]) < center_threshold_y:
        print("Center")
        requests.get(f"http://{host}/?cmd=s")  # Assuming 'c' is the command for center action
    elif abs(direction_vector[0]) > abs(direction_vector[1]):  # Horizontal movement
        if direction_vector[0] > 0:
            print("Left")
            requests.get(f"http://{host}/?cmd=l")
        else:
            print("Right")
            requests.get(f"http://{host}/?cmd=r")
    else:  # Vertical movement
        if direction_vector[1] > 0:
            print("Downward")
            requests.get(f"http://{host}/?cmd=b")
        else:
            print("Upward")
            requests.get(f"http://{host}/?cmd=f")

while True:
    success, image = cap.read()

    if not success:
        break

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_rgb)
    
    image_height, image_width, _ = image.shape
    # Draw the central square
    center_x, center_y = image_width // 2, image_height // 2
    square_size = 40
    top_left = (center_x - square_size, center_y - square_size)
    bottom_right = (center_x + square_size, center_y + square_size)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            nose_tip_landmark = face_landmarks.landmark[1]
            nose_tip = np.array([nose_tip_landmark.x * image_width, nose_tip_landmark.y * image_height])
            
            classify_head_position(nose_tip, image_width, image_height)
            
            cv2.circle(image, (int(nose_tip[0]), int(nose_tip[1])), 5, (0, 0, 255), -1)

    cv2.imshow('Camera 1 - Head Pose Estimation', image)

    if cv2.waitKey(5) & 0xFF in [27, ord('q')]:
        requests.get(f"http://{host}/?cmd=s")  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
