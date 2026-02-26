#GO AND STOP TIMER OR LOOP
import easyocr
import cv2
import requests

# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False)
host_bot=input("Enter brain block ip address : ")
# Function to send a string to the specified IP

#async def send_string_to_ip(data_to_send):
def send_string_to_ip(data_to_send):
 
    # Define the endpoint URL
    endpoint_url = f"http://{host_bot}/?cmd={data_to_send}"
 
    # Send a GET request with the command
    response = requests.get(endpoint_url)
    print(response)


# Open the BOT cam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Perform OCR on the frame
    result = reader.readtext(frame)

    # Extract the recognized text
    if result:
        text = result[0][1]
    else:
        text = "No text detected"
        send_string_to_ip("s")
    
    if all(char in text.lower() for char in ["s", "t", "o", "p"]):
        send_string_to_ip("s")
    elif all(char in text.lower() for char in ["g", "o"]):
        send_string_to_ip("f")
    elif all(char in text.lower() for char in ["r", "i", "g", "h", "t"]):
       send_string_to_ip("r")
    elif all(char in text.lower() for char in ["l", "e", "f", "t"]):
        send_string_to_ip("l")    
                 

    # Display the recognized text
    cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('OCR', frame)

    # Check for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
