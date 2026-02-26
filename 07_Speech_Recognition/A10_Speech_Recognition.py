import speech_recognition as sr
import re
import requests

host_bot=input("Enter brain block ip address : ")

def get_ultrasonic_value():
    ultrasonic_url = f"http://192.168.{bot_num}.10/?cmd=US"
    response = requests.get(ultrasonic_url)
    if response.status_code == 200:
        try:
            return int(response.text)
        except ValueError:
            return None
    return None

def recognize_speech_and_get_direction():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Regular expressions for direction commands
    right_pattern = re.compile(r"\b(right)\b", re.IGNORECASE)
    left_pattern = re.compile(r"\b(left)\b", re.IGNORECASE)
    forward_pattern = re.compile(r"\b(forward|straight|up)\b", re.IGNORECASE)
    backward_pattern = re.compile(r"\b(backward|back|behind)\b", re.IGNORECASE)

    # Capture data from the microphone
    with sr.Microphone() as source:
        print("Say a direction (right, left, forward, backward):")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        question = recognizer.recognize_google(audio_data)
        print("You said: " + question)
        
        ultrasonic_value = get_ultrasonic_value()
        
        if ultrasonic_value is not None and ultrasonic_value < 15:
            requests.get(f"http://{host_bot}/?cmd=b(200)")

        # Determine the direction based on the recognized speech
        elif right_pattern.search(question):
            requests.get(f"http://{host_bot}/?cmd=r(500)")
            return "Turn right"
        elif left_pattern.search(question):
            requests.get(f"http://{host_bot}/?cmd=l(500)")
            return "Turn left"
        elif forward_pattern.search(question):
            requests.get(f"http://{host_bot}/?cmd=f(500)")
            return "Go forward"
        elif backward_pattern.search(question):
            requests.get(f"http://{host_bot}/?cmd=b(500)")
            return "Go backward"
        else:
            return "Sorry, I didn't understand that direction."

    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

# Example usage
direction = recognize_speech_and_get_direction()
print(direction)
