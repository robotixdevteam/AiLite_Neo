import cv2
from deepface import DeepFace
import requests
import os
import keyboard
import tkinter as tk
from tkinter import filedialog



def get_image_paths():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title="Select images", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    return list(file_paths)  # Convert tuple to list

reference_images = get_image_paths()  # User selects multiple images at once

cap = cv2.VideoCapture(0)  # Primary camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

face_match = False

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        cv2.imwrite("current_frame.jpg", frame)
        for reference_img_path in reference_images:
            if not os.path.exists(reference_img_path):
                print(f"File not found: {reference_img_path}")
                continue
            try:
                result = DeepFace.verify("current_frame.jpg", reference_img_path)
                if result['verified']:
                    face_match = True
                    break
            except Exception as e:
                print("Verification failed:", e)

        if face_match:
            cv2.putText(frame, "Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            break

        cv2.imshow("Primary Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('z'):
            break
except Exception as e:
    print("Error in main loop:", e)
finally:
    cap.release()
    cv2.destroyAllWindows()
  

def get_ultrasonic_value():
    ultrasonic_url = f"http://192.168.{bot_num}.10/?cmd=US"
    response = requests.get(ultrasonic_url)
    if response.status_code == 200:
        try:
            return int(response.text)
        except ValueError:
            return None
    return None    

if face_match:
    print("Access Granted")  # Print "Access Granted" after exiting the loop
    
    print("Press and hold the 'up' arrow key to trigger the GET request. Press 'ESC' to exit.")
    
    host_bot=input("Enter brain block ip address : ")
    while True:
        # Check if the 'up' arrow key is pressed
        ultrasonic_value = get_ultrasonic_value()
        
        if ultrasonic_value is not None and ultrasonic_value < 15:
            requests.get(f"http://{host_bot}/?cmd=b(200)")
            
        elif keyboard.is_pressed('up'):
            requests.get(f"http://{host_bot}/?cmd=f")
            print("up")
        elif keyboard.is_pressed('down'):
            requests.get(f"http://{host_bot}/?cmd=b")
            print("down")
        elif keyboard.is_pressed('left'):
            requests.get(f"http://{host_bot}/?cmd=l")
            print("left")
        elif keyboard.is_pressed('right'):
            requests.get(f"http://{host_bot}/?cmd=r")
            print("right")
        elif keyboard.is_pressed('space'):
            requests.get(f"http://{host_bot}/?cmd=s")
            print("stop")           
        
    
        # Break the loop if 'ESC' is pressed to exit the program
        elif keyboard.is_pressed('esc'):
            requests.get(f"http://{host_bot}/?cmd=s")
            print("Exiting...")
            break

