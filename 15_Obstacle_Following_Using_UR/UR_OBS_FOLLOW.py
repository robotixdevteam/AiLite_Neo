import time
import http.client

host=input("Enter brain block ip address : ")
port = 80
us_path = f"/?cmd=US"
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

while True:
    left_1data = send_re_httpquest(host, port, us_path)
    left_data = int(left_1data)
    print(left_data)

    if left_data > 10 and left_data < 30 :
        #requests.get(f"http://{host_bot}/?cmd=f(200)")
        path=f"/?cmd=f(200)"
        send_re_httpquest(host, port, path) 
