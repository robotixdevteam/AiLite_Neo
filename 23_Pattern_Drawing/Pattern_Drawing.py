import time
import http.client

host_bot_bot = input("Enter brain block ip address : ")
port = 80

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

path = f"/?cmd=l(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=l(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=l(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=l(2000)"
send_re_httpquest(host_bot, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host_bot, port, path)
