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

# Example usage
host=input("Enter brain block ip address : ")
port = 80
right_ir_path = f"/?cmd=USLIR" 
left_ir_path= f"/?cmd=USRIR"

while True:
    left_data = send_re_httpquest(host, port, left_ir_path)
    print(left_data)
    right_data = send_re_httpquest(host, port, right_ir_path)
    print(right_data)
    if left_data is None or right_data is None:
        print("Failed to get data from sensors")
        continue

    try:
        left_ir = int(left_data[-1])
        right_ir = int(right_data[-1])
    except ValueError:
        print("Received invalid data from sensors")
        continue

    if left_ir == 1 and right_ir == 0:
        path = f"/?cmd=l(200)"
        send_re_httpquest(host, port, path)
    elif left_ir == 0 and right_ir == 1:
        path = f"/?cmd=r(200)"
        send_re_httpquest(host, port, path)
    elif left_ir == 0 and right_ir == 0:
        path = f"/?cmd=b(500)"
        send_re_httpquest(host, port, path)
        path = f"/?cmd=r(1000)"
        send_re_httpquest(host, port, path)

