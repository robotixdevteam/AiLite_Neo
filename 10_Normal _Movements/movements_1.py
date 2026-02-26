import requests

host_bot=input("Enter brain block ip address : ")

print("Forward - f | Backward - b | Left - l | Right - r")
i=input("Give Movements : ")
requests.get(f"http://{host_bot}/?cmd={i}(1000)") 
