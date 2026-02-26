import requests
import speech_recognition as sr
import time
import http.client
 

host = input("Enter brain block ip address : ")
port = 80
 
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
 
def act_yes():
    path1 = f"/?cmd=f(500)"
    send_re_httpquest(host, port, path1)
    path2 = f"/?cmd=b(500)"
    send_re_httpquest(host, port, path2)
 
def act_no():
    path3 = f"/?cmd=r(500)"
    send_re_httpquest(host, port, path3)
    path4 = f"/?cmd=l(1000)"
    send_re_httpquest(host, port, path4)
    path5 = f"/?cmd=r(500)"
    send_re_httpquest(host, port, path5)
 
# Initialize recognizer class
recognizer = sr.Recognizer()
 
# Capture data from the microphone
with sr.Microphone() as source:
    print("Say something!")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio_data = recognizer.listen(source)
    try:
        # Recognize speech using Google Web Speech API
        question = recognizer.recognize_google(audio_data)
        print("You said: " + question)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
# Use Together API with DeepSeek-R1 model
API_URL = "https://router.huggingface.co/together/v1/chat/completions"
headers = {
    "Authorization": "Bearer hf_wrsJaMfqQkviTxftOsNJBzLDeodRvm145", #Replace your API Key Here
}
 
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
 
# Prepare the question with strict yes/no requirement
formatted_question = f"{question} Answer strictly with only 'yes' or 'no' and nothing else."
 
response = query({
    "messages": [
        {
            "role": "user",
            "content": formatted_question
        }
    ],
    "model": "deepseek-ai/DeepSeek-R1"
})
 
# Extract the assistant's response
assistant_response = response["choices"][0]["message"]["content"]
 
# Remove the <think>...</think> part if present
if "<think>" in assistant_response and "</think>" in assistant_response:
    final_response = assistant_response.split("</think>")[1].strip()
else:
    final_response = assistant_response
 
# Clean up the response and make it uppercase for comparison
clean_response = final_response.strip().upper()
 
# Determine action based on response
if "YES" in clean_response:
    print("Yes")
    act_yes()
elif "NO" in clean_response:
    print("No")
    act_no()
else:
    print("Could not determine yes/no answer from response:", final_response)
