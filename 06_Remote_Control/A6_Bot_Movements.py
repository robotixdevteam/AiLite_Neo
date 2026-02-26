import requests
import keyboard
import time
import http.client
bot_num = input("Enter bot number : ")
speed = int(input("Enter speed Limit between (150-250) : ")) 
print("Press and hold the 'up' arrow key to trigger the GET request. Press 'ESC' to exit.")
host_bot=input("Enter brain block ip address : ")
port = 80
us_path = f"/?cmd=US"


def send_re_httpquest(host_bot, port, path):
    """Send HTTP request with retries."""
    retries = 10  # Number of retries
    for _ in range(retries):
        conn = None
        try:
            conn = http.client.HTTPConnection(host_bot, port)
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

requests.get(f"http://{host_bot}/?cmd=left_speed={speed}")
requests.get(f"http://{host_bot}/?cmd=right_speed={speed}")

while True:
    # Check if the 'up' arrow key is pressed
    
    left_1data = send_re_httpquest(host_bot, port, us_path)
    left_data = int(left_1data)
    #print(left_data)

    if left_data <10 :
        #requests.get(f"http://{host_bot}/?cmd=f(200)")
        path=f"/?cmd=s"
        send_re_httpquest(host_bot, port, path)
        requests.get(f"http://{host_bot}/?cmd=b(100)") 

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
    else :
        requests.get(f"http://{host_bot}/?cmd=s")
