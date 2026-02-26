import cv2
import math
import time
import requests
from ultralytics import YOLO

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#
# delay in seconds
intervel = 0.01
host = input("Enter brain block ip address : ")
cam_host = input("Enter camera ip address : ")

def delay(sec):
    time.sleep(sec)

def bot_move(com):
    try:
        response = requests.get(f"http://{host}/?cmd={com}")
        if response.status_code == 200:
            print(f"bot_move({com})")
        else:
            print(f"Failed to send command. HTTP Status Code: {response.status_code}")
        delay(intervel)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception - Move: {err}")

def bot_speed(l_pwm, r_pwm):
    print(f"bot_speed(L : {l_pwm} | R : {r_pwm})")
    try:
        response = requests.get(f"http://{host}/?cmd=setspeed={l_pwm, r_pwm}")
        if response.status_code == 200:
            pass
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception - Speed: {err}")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

bb_size = 150

turn_delay = 100
D90_turn_delay = 500

speed_val = 130
pwm_corr = 5

def delay(sec):
    time.sleep(sec)

def initial_forward(bool):
    if bool == "true":
        bot_move("f")
        print("Initial Forward")

def stop():
    bot_move("s")
    print("stop")

def sign_detection(classname, wid, hght):
    if classname == "go":
        bot_move(f"f(500)")
    elif classname == "left":
        bot_move(f"l({D90_turn_delay})")
        # bot_move(f"lf({D90_turn_delay})")
    elif classname == "right":
        bot_move(f"r({D90_turn_delay})")
        # bot_move(f"rf({D90_turn_delay})")
    elif classname == "stop":
        bot_move("s")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

# Colour Codes
blue = (255, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# Start webcam
cap = cv2.VideoCapture(0)

MODEL = YOLO("Models/turn-signs-v4_640_yolov8_epo_100.pt")
CONFIDENCE_SCORE = 0.80
CLASS_NAME = ['go', 'left', 'right', 'stop']
CLASS_FILTER = [1]

# Variables for FPS calculation
start_time = time.time()
frame_count = 0
obj_count = 0

# Initial forward move
initial_forward("true")

while True:
    success, img = cap.read()
    if not success:
        break
    # Increment frame count for FPS calculation
    frame_count += 1

    model = MODEL
    results = model(source=img, conf=CONFIDENCE_SCORE)

    # Coordinates
    for r in results:
        boxes = r.boxes
        for box in boxes:
            obj_count += 1

            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to int values

            # Put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), green, 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            conf = str(int(confidence * 100))

            # Class name
            cls = int(box.cls[0])

            # Bounding box size
            width = x2 - x1
            height = y2 - y1
            print(CLASS_NAME[cls] + " Size : {} x {}".format(width, height))

            # Initial forward
            initial_forward("false")
            print("m_count : " + str(obj_count))

            if obj_count >= 4:
                sign_detection(CLASS_NAME[cls], width, height)
                obj_count = 0

            # Display Bounding Box Size on the screen
            text_size = "Size: {} x {}".format(width, height)
            cv2.putText(img, text_size, (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cyan, 2)

            # Object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = magenta
            thickness = 2

            textcv = CLASS_NAME[cls] + ":" + conf + " %"
            cv2.putText(img, textcv, org, font, fontScale, color, thickness)

    # Calculate FPS
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time

    # Display FPS on the screen
    cv2.putText(img, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, cyan, 2)
    cv2.imshow('Bot Webcam', img)

    if cv2.waitKey(1) == ord('q'):
        print("Quit 'q' was pressed.")
        stop()
        break

cap.release()
cv2.destroyAllWindows()
