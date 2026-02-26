import cv2
import numpy as np
import tensorflow as tf
import requests
import time
import http.client
def send_re_httpquest(host, port, path):
    """Send HTTP request with retries."""
    retries = 10  # Number of retries
    for _ in range(retries):
        conn = None
        try:
            conn = http.client.HTTPConnection(host, port)
            conn.request("GET", path)
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            if _ < retries - 1:
                time.sleep(1)
        finally:
            if conn:
                conn.close()
    return None  # Return None if all retries fail


def get_ultrasonic_value():
    ultrasonic_url = f"http://192.168.{bot_num}.10/?cmd=US"
    response = requests.get(ultrasonic_url)
    if response.status_code == 200:
        try:
            return int(response.text)
        except ValueError:
            return None
    return None 


host=input("Enter brain block ip address : ")
port = 80

# Load your trained model
model = tf.keras.models.load_model('emotion_detection_model.h5')
 
# Define the list of emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
 
# Initialize the face detector (Haar cascades)
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
# Start capturing video from the webcam
cap = cv2.VideoCapture(0)
 
while True:
    # Read the current frame from the webcam
    
    ultrasonic_value = get_ultrasonic_value()
        
    if ultrasonic_value is not None and ultrasonic_value < 15:
        print(ultrasonic_value)
        path = f"/?cmd=b(150)"
        send_re_httpquest(host, port, path)
    
    ret, frame = cap.read()
    if not ret:
        break
 
    # Convert the frame to grayscale (required for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Detect faces in the frame
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
 
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
       
        # Extract the region of interest (ROI) from the grayscale frame
        # Extract the region of interest (ROI) from the grayscale frame
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
 
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float')/255.0
            roi = tf.expand_dims(roi, axis=0)
            roi = tf.expand_dims(roi, axis=-1)
 
            # Predict the emotion
            predictions = model.predict(roi)
            max_index = np.argmax(predictions)
            predicted_emotion = emotion_labels[max_index]
            print(predicted_emotion)
 
            # Display the predicted emotion
            cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            
            
            if predicted_emotion=='Happy':
               path = f"/?cmd=r(1000)"
               send_re_httpquest(host, port, path)
            elif predicted_emotion=='Sad':
               path = f"/?cmd=b(1000)"
               send_re_httpquest(host, port, path)
            elif predicted_emotion=='Neutral':
               path = f"/?cmd=s"
               send_re_httpquest(host, port, path) 
            elif predicted_emotion=='Surprise':
               path = f"/?cmd=l(1000)"
               send_re_httpquest(host, port, path)
            elif predicted_emotion=='Angry':
               path = f"/?cmd=l(500)"
               send_re_httpquest(host, port, path)
               path = f"/?cmd=r(500)"
               send_re_httpquest(host, port, path)
            elif predicted_emotion=='Disgust':
               path = f"/?cmd=f(500)"
               send_re_httpquest(host, port, path)
               path = f"/?cmd=b(500)"
               send_re_httpquest(host, port, path)
            elif predicted_emotion=='Fear':
               path = f"/?cmd=f(500)"
               send_re_httpquest(host, port, path)
               path = f"/?cmd=l(500)"
               send_re_httpquest(host, port, path)
            else:
               path = f"/?cmd=s"
               send_re_httpquest(host, port, path)                        
 
 
    # Display the frame
    cv2.imshow('Emotion Detector', frame)
 
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
