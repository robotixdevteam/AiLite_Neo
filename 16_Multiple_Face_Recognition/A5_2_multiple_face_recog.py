import cv2
from deepface import DeepFace
import os
import keyboard
import requests
import tkinter as tk
from tkinter import filedialog


def get_directory_path(name):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    dir_path = filedialog.askdirectory(title=f"Select directory for {name}")
    return dir_path

# Define directories for each person with their names
people = ["Person_1", "Person_2", "Person_3"]
reference_images = {person: get_directory_path(person) for person in people}

print("Please face the camera and be steady")

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capture a single frame
ret, frame = cap.read()
if not ret:
    print("Failed to capture frame")
else:
    # Save the captured frame to a file
    cv2.imwrite("current_frame.jpg", frame)
    print("Image captured, proceed with verification.")

# Release the webcam
cap.release()

match_found = False  # Initialize match_found for each iteration
matching_name = ""

for name, dir_path in reference_images.items():
    if not os.path.exists(dir_path):
        print(f"Directory not found: {dir_path}")
        continue

    for image_filename in os.listdir(dir_path):
        image_path = os.path.join(dir_path, image_filename)

        try:
            result = DeepFace.verify("current_frame.jpg", image_path)
            if result['verified']:
                match_found = True
                matching_name = name
                print(f"Welcome {name}")
                break
        except Exception as e:
            print("Verification failed:", e)

    if match_found:
        break

# Action based on match result
if match_found:
    if matching_name in ["Person_1", "Person_2"]:
        print("Use arrow keys to control the bot. Press 'ESC' to exit.")
        
        host = input("Enter brain block ip address : ")
        port = 80

        while True :        
            
            
            if keyboard.is_pressed('up'):
                print("Forward")
                requests.get(f"http://{host}/?cmd=f")
            elif keyboard.is_pressed('down'):
                print("Backward")
                requests.get(f"http://{host}/?cmd=b") 
            elif keyboard.is_pressed('left'):
                print("left") 
                requests.get(f"http://{host}/?cmd=l")
            elif keyboard.is_pressed('right'):
                print("right")
                requests.get(f"http://{host}/?cmd=r")
            elif keyboard.is_pressed('space'):
                print("stop")
                requests.get(f"http://{host}/?cmd=s")    
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                requests.get(f"http://{host}/?cmd=s")
                break
            else:
                requests.get(f"http://{host}/?cmd=s") 
                

    elif matching_name == "Person_3":
        print("Unfortunately, you don't have a driving licence to drive the bot. Sorry for the inconvenience.")
else:
    print("No valid face match found. Access denied.")

