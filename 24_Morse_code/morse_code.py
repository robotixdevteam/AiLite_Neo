import time
import http.client


host = input("Enter brain block ip address : ")
port = 80
us_path = "/?cmd=USRIR"
time.sleep(2)  # Wait for 5 seconds before the next iteration

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

# Run the loop for a specified duration (e.g., 1 minute)

#f = 0010

#b = 1000

#l = 0100

#r = 0101

#d = 1001

movements = ""


duration = 4  # Total duration in seconds
start_time = time.time()

while time.time() - start_time < duration:
    touch_value = send_re_httpquest(host, port, us_path)
    if touch_value == "Right US IR Value: 1":
        value = 0
        movements = movements + str(value)
    else:
        value = 1
        movements = movements + str(value)   
    print(value)
    time.sleep(1)  # Wait for 5 seconds before the next iteration
print(movements)
if movements == "0010":
    path=f"/?cmd=f(500)"
    send_re_httpquest(host, port, path)
elif movements == "1000":
    path=f"/?cmd=b(500)"
    send_re_httpquest(host, port, path)
elif movements == "0100":
    path=f"/?cmd=l(500)"
    send_re_httpquest(host, port, path)
elif movements == "0101":
    path=f"/?cmd=r(500)"
    send_re_httpquest(host, port, path)
elif movements == "1001":
    path=f"/?cmd=r(2000)"
    send_re_httpquest(host, port, path)
    path=f"/?cmd=f(1000)"
    send_re_httpquest(host, port, path)
    path=f"/?cmd=l(2000)"
    send_re_httpquest(host, port, path)
    
