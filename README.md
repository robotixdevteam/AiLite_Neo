<p align="center" width="80%">
<img width="30%" src="AILITE IMAGE/AILITE LOGO.png" />
</p>


<p align="center" width="80%">
<img width="60%" src="Ailite_neo2.JPG" />
</p>

 AILite Neo is a cutting-edge autonomous robot designed for a wide range of applications. With its sophisticated four-wheel drive system, integrated camera, ultrasonic sensors, IR sensor, color sensor, and touch sensor, AILite is capable of navigating complex environments with precision and intelligence. This versatile bot is perfect for tasks requiring advanced obstacle detection, machine learning applications, and real-time monitoring, making it an ideal solution for both educational and industrial purposes.MIT App Inventor is used for the execution of the projects.

## Get the Source Code
You can download the repository as a [zip file](https://github.com/marreddyanuhya/AILITE-MIT-APPLICATIONS/archive/refs/heads/main.zip) and extract it into a folder of your choice.

## Setting up the Local Connection
#  First, turn on wifi in Laptop/PC.
   Make sure to have wifi enabled laptop/pc

#  Ailite neo hub connection  :

Turn on the AiLite Neo bot, that acts as the hotspot. Establish connection by entering the `WiFi-Name = 'AILITE-<unique-ID>' (for example, 'AILITE-1034')` and `Wifi-Password = '12345678'`.

Accessing Unique URL for each AiLite Neo Bot:

- In web browser kindly enter the below url for accessing AiLite bot in web url.

        
        192.168.{bot_number}.10
        
  -For example 'AILITE-0134' here inverse of last four number is the bot number

        
        192.168.43.10

  -Then in the url we will get an webpage where we need to enter our wifi crediantials details (Wifi name & Password).
   Make sure we have a wifi connection with internet or we can use mobile hotspot with internet.
   Wifi connection with 5G is not preffered.

  -After entering the wifi crediantials , once it is successfully connected we will get Ailite neo hub host url .(For example : 162.189.12.10) make sure to copy this url which will be used    in program.

#  Ailite neo camera connection  : Same as the hub connection.

Turn on the AiLite Neo camera, that acts as the hotspot. Establish connection by entering the `WiFi-Name = 'Camera-<unique-ID>' (for example, 'Camera-1034')` and `Wifi-Password = '12345678'`.

Accessing Unique URL for each AiLite Neo camera:

- In web browser kindly enter the below url for accessing AiLite camera in web url

        192.168.{bot_number}.10
        
  -For example 'Camera-0134' here inverse of last four number is the bot number

        
        192.168.43.10

  -Then in the url we will get an webpage where we need to enter our wifi crediantials details (Wifi name & Password). Make sure we have a wifi connection with internet or we can use mobile hotspot    with internet. Wifi connection with 5G is not preffered.

  -After entering the wifi crediantials , once it is successfully connected we will get Ailite neo camera host url(For example : 162.189.12.10) make sure to copy this url which will be used in program .

#  Final Setup

Once both the **AILite Neo Hub** and **AILite Neo Camera** are connected to the same WiFi network:

1. Disconnect from the temporary hotspot.
2. Connect your laptop/PC to the **same WiFi network** used for the robot and camera.
3. You are now ready to start working with the **AILite Neo system**.

---

## Table of Contents
-[MIT App Inventor Installation](#MIT-App-Inventor-Installation)

-[MIT Projects Overview](#MIT-Projects-Overview)

## MIT App Inventor Installation
Here's a guide on how to install MIT App Inventor
### Installing MIT App Inventor
MIT App Inventor is a cloud-based tool that allows you to create Android apps using a visual programming interface.
Follow these steps to set up MIT App Inventor on your computer:

## Step 1: Set Up a Google Account
MIT App Inventor requires a Google account to log in and save your projects. 
If you don’t already have one, you can create a Google account at accounts.google.com/signup.

## Step 2: Access MIT App Inventor
Open your web browser (Chrome is recommended for the best experience).
Go to the MIT App Inventor website: appinventor.mit.edu.
Click on the “Create Apps!” button to be redirected to the App Inventor interface.
Log in using your Google account credentials.

## Step 3: Connect Your Android Device
To test your apps, you can connect your Android device in one of three ways:

### AI Companion App: 
The simplest method is to download the MIT AI2 Companion app from the Google Play Store on your Android device.
Open the app on your device.
In the MIT App Inventor interface, click “Connect” and select “AI Companion.”
Scan the QR code that appears on your computer screen with the AI2 Companion app.

### USB Connection:
Connect your Android device to your computer via USB.
Click on “Connect” and select “USB” in the MIT App Inventor interface.

### Emulator: 
If you don't have an Android device, you can use an Android emulator on your computer.
Click on “Connect” and select “Emulator.”

## Step 4: Start Creating Your App
Once connected, you can start building your app by dragging and dropping components in the Designer and programming their behavior in the Blocks Editor.

## MIT Projects Overview
### 1. Artist AILite
- **Objective**:The Artist AILite feature enables the system to recognize shapes such as straight lines or alphabets drawn by the user, and then replicate those shapes.
- **Sensor**: Phone Camera-Machine Learning

### 2. Button control-L1(Level 1)
- **Objective**: In the button control feature, clicking the Start Button activates forward motor movement, while clicking the Stop Button halts motor operation.


### 3. Button control-L2 (Level 2)
- **Objective**:	It Use buttons to control AiLite's movements.

### 4. Chatbot 
- **Objective**: It performs operations based on yes/no questions, providing responses accordingly.
- **Sensor**: Phone's Mic - Text to Speech & Speech Recognition

### 5. Emotion Recognition-L1	
- **Objective**: The emotion recognition feature detects whether the user is happy or angry. If the user is happy, AILite initiates a dance, whereas if the user is angry, AILite moves away from the user.
- **Sensor**: Phone Camera - Machine Learning


### 6. Face detection
- **Objective**:By using Personal Image Classifier it enables AILite to dance when a face is detected through camera, and spin around when no face is detected.
- **Sensor**: Phone Camera - Machine Learning

### 7.	Face Recognition-Hi user
- **Objective**:	AILite detects its user and say "Hi User" and do some actions, if not its user it say "you are not my user" and go away.
- **Sensor**: Phone Camera - Machine Learning

### 8.	Hand Gestures 
- **Objective**: Open and close hand	By recognizing hand gestures, AiLite performs predefined actions, using personal image classifier
- **Sensor**: Phone Camera - Machine Learning**

### 9.	Light sensor control
- **Objective**: This makes the bot move forward in the presence of light and halt when there is no light.
- **Sensor**: Phone LDR Sensor

### 10.	Object Follower-US
- **Objective**: It uses Ultrasonic sensor to detect the objects and follows the Object.
- **Sensor**: Bot's Ultrasonic Sensor

### 11.	Obstacle Avoider-IR
- **Objective**: It Include TTS(Test to Speech) It uses IR sensor values to detect and avoid obstacles in front of it, and informs the user if an obstacle is present.
- **Sensor**: Bot's IR Sensor

### 12.	OCR App
- **Objective**: Speed control	It Recognizes characters and adjust the speed of AILite accordingly.
-**Sensor**: Phone Camera - Text Recognition

### 13.	Orientation Sensor-Compass
- **Objective**: This uses compass directions to guide AiLite Neo in performing specific actions based on its orientation.
- **Sensor**: Phone Accelerometer

### 14.	Remote Surviellance
- **Objective**: The user initiates remote surveillance using buttons for "forward," "backward," "left," and "right." The ESP32 camera streams the footage, enabling control of the bot's movements forward and backward.
- **Sensor**: Bot Camera

### 15.	Specs Recognition
- **Objective**: AILite Neo recognizes the specs and do some actions by using Teachable Machines.
- **Sensor**: Phone Camera - Machine Learning

### 16.	Speech control AILite-L1 (Level 1)
- **Objective**: In Speech Control, users can prompt AILite Neo to "start moving" to initiate motion and "stop moving" to halt it, facilitating seamless interaction.
- **Sensor**: Phone's Mic

### 17.	Speech control AILite-L2 (Level 2)
- **Objective**:	The user gives voice commands like "move forward," "move backward," and more, which AiLite Neo processes to perform the corresponding actions.
- **Sensor**: Phone's Mic

### 18.	Speed Control Ailite
- **Objective**:AILite Neo adjusts between low, medium, and high speeds through button controls.

### 19. Swipe 	Gesture Control
- **Objective**:	It utilizes swipe gestures for movement control.
- **Sensor**: Phone's Touch Control

### 20.	Tilt Control AILite-L1 (Level 1)
- **Objective**: This enables the bot to turn left when the phone is tilted left and turn right when the phone is tilted right.
- **Sensor**: Phone Accelerometer

### 21.	Tilt control AILite-L2 (Level 2)
- **Objective**:The user tilts the device forward for forward movement, backward for backward movement, and more, AILite neo implements the actions accordingly.
- **Sensor**: Phone Accelerometer

### 22.	Traffic sign Detection
- **Objective**: Using personal Image classifier, AiLite adjusts its movements based on recognized traffic signs.
- **Sensor**: Phone Camera - Machine Learning

### 23.	WorkoutBuddy-Pedometer
- **Objective**: The pedometer feature enables AILite neo to follow the user's walking motion; when the user starts walking, AILite neo initiates movement, and when the user stops, AILite neo halts as well. Additionally, it tracks the number of steps taken, distance covered, and elapsed time during the activity.
- **Sensor**: Phone Accelerometer

### 24. Action Gen AI
- **Objective**:Users can control Ailite Neo by giving commands such as move forward, move backward, and other actions, effectively providing it with a brain and sensor-based control system.

### 25. Characters
- **Objective**: This features three characters—Owl, Crab, and Bat—each with a unique personality: Mentor, Teacher, and Friend. Users can interact with these characters to ask questions and engagingly learn STEM subjects.

### 26. Conversational ChatBots
- **Objective**:Users can interact with the LLM through a chat interface, where the conversation history is saved for each session.

### 27. Conversational ChatBot KB
- **Objective**: Users can upload their own knowledge base to the LLM and perform tasks such as question-and-answer sessions and summarization using their data.

### 28. Shapes
- **Objective**: This application has two modes. In the first mode, users can draw predefined shapes such as circles, squares, and triangles. In the second mode, users can draw shapes freely using button controls, and our AI model analyzes the drawing to identify the shape.

### 29. Text Gen AI
- **Objective**:In this program, users can enter their queries as text input and receive relevant text-based responses. We have used OpenAI as the large language model (LLM) to generate the outputs.

### 30. yes no neo 
- **Objective**:Ailite Neo asks questions to the user and performs actions based on the user’s response. If the response is correct, it rotates its tail; if the response is incorrect, it rotates its head.

  
## Types of construction
### 2-Wheel Construction

The 2-wheel construction is a popular and widely used design in AILite Neo projects. It is favored for its simplicity, agility, and versatility, making it suitable for a broad range of applications. This design features two wheels driven by motors, allowing for straightforward movement and maneuverability. The 2-wheel version is especially well-suited for projects that require quick directional changes, precise navigation, and efficient use of space.

Key Features:
Versatility: The 2-wheel construction can be applied to a wide variety of projects, ranging from basic robotics to more complex automation tasks.
Agility: With only two wheels, this design allows for easy turning and swift movement, making it ideal for navigating tight spaces and performing tasks that require quick adjustments.
Simplicity: The design is simple, making it easier to build, maintain, and modify for different project needs.

### 4-Wheel Construction

The 4-wheel construction in AILite Neo provides a more stable and robust platform, which is particularly advisable for projects involving color sensors and other sensor-based applications. While the same projects that can be performed with the 2-wheel version can also be executed with the 4-wheel version, the latter offers added stability and support, which is crucial for certain types of sensor-based tasks.

Key Features:
Stability: The 4-wheel design offers greater stability, reducing the risk of tipping or imbalance, especially when navigating uneven terrain or carrying additional sensors and equipment.
Enhanced Sensor Performance: For color sensor-based projects, the 4-wheel construction provides a steadier platform, ensuring more accurate sensor readings and reliable performance.
Adaptability: Although more complex than the 2-wheel version, the 4-wheel construction can handle the same range of projects, with the added benefit of increased stability and sensor integration.

## Various Execution Options for AILite Neo

In addition to MIT App Inventor, AILite Neo projects can also be developed using Python, a powerful and user-friendly platform for creating mobile applications. MIT App Inventor allows users to design and implement projects through a visual programming interface, making it accessible to those who may not be familiar with traditional coding. Kindly refer the following link for more information.


## Contact

- Contact us via [Email](mailto:development@merituseducation.com)
















