# AiLite
<p align="center" width="80%">
    <img width="40%" src="AiLite.JPG" />
</p>

AILite is a cutting-edge autonomous robot designed for a wide range of applications. With its sophisticated four-wheel drive system, integrated camera, ultrasonic sensors, IR sensor, color sensor, and touch sensor, AILite is capable of navigating complex environments with precision and intelligence. 

# Connection

## How to Set up the Local Connection:

1. First, turn on wifi in Laptop/PC.

2. Ailite neo hub connection  :

Turn on the AiLite Neo bot, that acts as the hotspot. Establish connection by entering the `WiFi-Name = 'AILITE-<unique-ID>' (for example, 'AILITE-1034')` and `Wifi-Password = '12345678'`.

Accessing Unique URL for each AiLite Neo Bot:

- In web browser kindly enter the below url for accessing AiLite bot in web url.

        
        192.168.{bot_number}.10
        
  -For example 'AILITE-0134' here inverse of last four number is the bot number

        
        192.168.43.10

  -Then in the url we will get an webpage where we need to enter our wifi crediantials details (Wifi name & Password). Make sure we have a wifi connection with internet or we can use mobile hotspot with internet. Wifi connection with 5G is not preffered.

  -After entering the wifi crediantials , once it is successfully connected we will get Ailite neo hub host url .(For example : 162.189.12.10) make sure to copy this url which will be used in program.

3. Ailite neo camera connection  : Same as the hub connection.

Turn on the AiLite Neo camera, that acts as the hotspot. Establish connection by entering the `WiFi-Name = 'Camera-<unique-ID>' (for example, 'Camera-1034')` and `Wifi-Password = '12345678'`.

Accessing Unique URL for each AiLite Neo camera:

- In web browser kindly enter the below url for accessing AiLite camera in web url

        192.168.{bot_number}.10
        
  -For example 'Camera-0134' here inverse of last four number is the bot number

        
        192.168.43.10

  -Then in the url we will get an webpage where we need to enter our wifi crediantials details (Wifi name & Password). Make sure we have a wifi connection with internet or we can use mobile hotspot    with internet. Wifi connection with 5G is not preffered.

  -After entering the wifi crediantials , once it is successfully connected we will get Ailite neo camera host url(For example : 162.189.12.10) make sure to copy this url which will be used in program .
        

## You first need to setup your environment.

## Dependencies

We recommend to create a conda environment for AiLIte. Instructions on installing conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/). The easiest way to create a new environment with all dependencies is to use one of the provided environment files. 
Make sure it you create conda environmen and download requirements.txt in the projects folder path.
### Environment Setup

First create a new conda environment with the following command:

```bash
conda tos view
```

```bash
conda tos accept
```

```bash
conda create -n <environment_name> python=3.11 -y
```

Next, you need to activate your conda environment:

```bash
conda activate <environment_name>
```

Once your environment is active, need to install requirements for each projects

#### **Windows**
```
pip install -r requirements.txt
```
#### **Linux**
```
pip install -r requirements.txt
```

#### **Mac**
```
pip install -r requirements.txt
```
### Notes

- Remember to activate the environment, before you execute your python programs. Give the below command to run python program.

```bash
python <script_name.py>
```

# Below is a list of all the projects included in this repository.

# 1. Object Detection 

This project is designed to detect and recognize traffic signs using YOLO (You Only Look Once) object detection and then control a bot accordingly based on the detected sign.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/01_Object_Detection)

# 2. Text Recognition 

This program utilizes OCR (Optical Character Recognition) to detect text from a webcam feed and control a bot accordingly. It can recognize commands like "go" and "stop" and send corresponding signals to a specified IP address.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/02_Text_Recognition)

# 3. Gesture Recognition 

This script utilizes the Mediapipe library to perform hand gesture recognition using a webcam feed. It detects various hand gestures and sends corresponding commands to a specified host.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/03_Gesture_Recognition)

# 4. Face Motion Detection 

This script utilizes MediaPipe's Face Mesh model to estimate the pose of a person's head using their nose tip landmark. Based on the head pose, it sends corresponding commands to a specified host, allowing for head-controlled actions.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/04_Face_Motion_Detection)

# 5. Face Recognition 

This script performs face recognition using the DeepFace library and grants access based on the recognized faces. If a face in the captured frame matches any of the reference images, access is granted and commands can be triggered using keyboard inputs.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/05_Face_Recognition)

# 6. Remote Control 

This script allows you to control a bot using keyboard inputs. You can use arrow keys to move the bot in different directions and the space key to stop it. Press 'ESC' to exit the program.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/06_Remote_Control)

# 7. Speech Recognition 

This script allows you to control a bot using voice commands. You can give commands such as "turn right", "turn left", "go forward", or "go backward" using your microphone.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/07_Speech_Recognition)

# 8. Face Emotion Detection 

This project is an emotion detection system using a webcam and a trained deep learning model. The detected emotions trigger specific HTTP requests to control a robot.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/08_Face_Emotion_Detection)

# 9. Tic Tac Toe 

This project implements a simple Tic Tac Toe game with a graphical user interface (GUI) using the Tkinter library in Python. The game allows a human player to play against the computer.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/09_Tic_Tac_Toe)

# 10. Normal Movements 

This Python script allows you to control a robot over a network using simple HTTP requests. You can send commands to move the robot forward, backward, left, or right.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/10_Normal%20_Movements)

# 11. Yes No Bot Movements 

This Python script conducts a simple quiz and controls a robot over a network based on the user's answers. It sends HTTP requests to move the robot forward or backward depending on the user's responses.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/11_Yes_No_Bot_Movements)

# 12. Stone Paper Scissors 

This Python script implements a Stone Paper Scissors game using a graphical user interface (GUI) with Tkinter. The game includes functionality to control a robot over a network based on the computer's choice using HTTP requests.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/12_Stone_Paper_Scissors)

# 13. Speed Control 

This Python script allows you to control a robot over a network using keyboard inputs. It sends HTTP GET requests to move the robot forward, backward, left, or right, and allows you to adjust the speed. The script also includes functionality to stop the robot and exit the program.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/13_Speed_Control)

# 14. Obstacle Avoider Using IR 

This Python script allows you to control a robot over a network using data from infrared (IR) sensors. It sends HTTP GET requests to navigate the robot based on the sensor data received.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/14_Obstacle_Avoider_Using_IR)

# 15. Obstacle Following Using UR 

This Python script allows you to control a robot using data from an ultrasonic (US) sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/15_Obstacle_Following_Using_UR)

# 16. Multiple Face Recognition 

This script performs face recognition using the DeepFace library and grants access based on the recognized faces. If a face in the captured frame matches any of the reference images, access is granted and commands can be triggered using keyboard inputs.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/16_Multiple_Face_Recognition)

# 17. Teachable Machine Color Recognition 

This project uses a neural network model to control a robot based on the detected color of a traffic light in a webcam feed. If the model detects a "GREEN" light, it sends a command to the robot to move forward. If the model detects a "RED" light, it sends a command to the robot to stop.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/17_Teachable_Machine_Color_Recognition)

# 18. Teachable Machine Face Recognition 

This Python script utilizes a deep learning model to recognize faces through a webcam feed and controls a device based on the recognized individual. It's designed to interact with a remote device by sending HTTP requests to trigger actions like moving forward or backward<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/18_Teachable_Machine_Face_Recognition)

# 19. Survilence Bot 

This script allows you to control a bot using keyboard inputs. You can use arrow keys to move the bot in different directions and the space key to stop it. Press 'ESC' to exit the program.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/19_Survilence_Bot)

# 20. AiLite Chatbot 

This Python application allows users to control a robot through voice commands, leveraging advanced speech recognition and decision-making model integration. It is particularly designed for interactive scenarios where voice input can dictate robot actions.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/20_AiLite_Chatbot)

# 21. Binary Digits 

This Python script allows you to control a robot using binary digits 0s and 1s. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/21_Binar_Digits)

# 22. Go Stop 

This Python script allows you to control a robot using data from Color sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/22_Go_Stop)

# 23. Pattern Drawing 

This Python script allows bot to draw a pattern. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/23_Pattern_Drawing)

# 24. Morse Code 

This Python script allows bot to draw a pattern. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/robotixdevteam/AiLite/tree/Python/24_Morse_code)






## Types of construction
## 2-Wheel Construction

The 2-wheel construction is a popular and widely used design in AILite projects. It is favored for its simplicity, agility, and versatility, making it suitable for a broad range of applications. This design features two wheels driven by motors, allowing for straightforward movement and maneuverability. The 2-wheel version is especially well-suited for projects that require quick directional changes, precise navigation, and efficient use of space.

Key Features:
Versatility: The 2-wheel construction can be applied to a wide variety of projects, ranging from basic robotics to more complex automation tasks.
Agility: With only two wheels, this design allows for easy turning and swift movement, making it ideal for navigating tight spaces and performing tasks that require quick adjustments.
Simplicity: The design is simple, making it easier to build, maintain, and modify for different project needs.

## 4-Wheel Construction

The 4-wheel construction in AILite provides a more stable and robust platform, which is particularly advisable for projects involving color sensors and other sensor-based applications. While the same projects that can be performed with the 2-wheel version can also be executed with the 4-wheel version, the latter offers added stability and support, which is crucial for certain types of sensor-based tasks.

Key Features:
Stability: The 4-wheel design offers greater stability, reducing the risk of tipping or imbalance, especially when navigating uneven terrain or carrying additional sensors and equipment.
Enhanced Sensor Performance: For color sensor-based projects, the 4-wheel construction provides a steadier platform, ensuring more accurate sensor readings and reliable performance.
Adaptability: Although more complex than the 2-wheel version, the 4-wheel construction can handle the same range of projects, with the added benefit of increased stability and sensor integration.

## Various Execution Options for AILite

In addition to Python, AILite projects can also be developed using MIT App Inventor, a powerful and user-friendly platform for creating mobile applications. MIT App Inventor allows users to design and implement projects through a visual programming interface, making it accessible to those who may not be familiar with traditional coding. Kindly refer the follwing link for more information.


## Contact

- Contact us via [Email](mailto:development@merituseducation.com)





