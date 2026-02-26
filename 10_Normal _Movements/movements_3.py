import requests

host_bot=input("Enter brain block ip address : ")

while True:
    print("Forward - f | Backward - b | Left - l | Right - r")
    i=input("Give Movements : ")
    if i =="f" or i=="b":
       requests.get(f"http://{host_bot}/?cmd={i}(1000)") 
    elif i=="l" or i=="r":
        requests.get(f"http://{host_bot}/?cmd={i}(500)")
    else:
        print("Invalid Movements")      
