import time
import re
import http.client

host_bot_bot = input("Enter brain block ip address : ")
port = 80
cs_path = f"/?cmd=cs"

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

outer_loop = True

path = f"/?cmd=lf_speed=180"
send_re_httpquest(host_bot, port, path)

path = f"/?cmd=lb_speed=180"
send_re_httpquest(host_bot, port, path)

path = f"/?cmd=rf_speed=180"
send_re_httpquest(host_bot, port, path)

path = f"/?cmd=rb_speed=180"
send_re_httpquest(host_bot, port, path)


def colorfinder(value):
    if value >4000 and value <4800 :
        return "r"
    elif value >5100 and value <6000:
        return "g"    
    # elif value >9200 and value <14000:
    #     return "r" 
    # elif value >3600 and value <4000:
    #     return "bl" 
    # elif value >10000 and value <10900:
    #     return "w" 

while True : 
    path = f"/?cmd=s"
    send_re_httpquest(host_bot, port, path)
    input_string = send_re_httpquest(host_bot, port, cs_path)
    match = re.search(r'C:\s*(\d+)', input_string)
    c_value = int(match.group(1))
    print(c_value)
    predicted_color = colorfinder(c_value)
    print(predicted_color)
    
    if predicted_color == "g":
       path = f"/?cmd=f(200)"
       send_re_httpquest(host_bot, port, path)
       path = "/?cmd=s"
       send_re_httpquest(host_bot, port, path) 
    
    elif predicted_color == "r":
        path = f"/?cmd=s"
        send_re_httpquest(host_bot, port, path)
        
    else:
        path = "/?cmd=f(200)"
        send_re_httpquest(host_bot, port, path)
        path = "/?cmd=s"
        send_re_httpquest(host_bot, port, path)    
               
        
    time.sleep(1)          

