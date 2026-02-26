import requests
import keyboard

print("Press and holdl the 'up' arrow key to trigger the GET request. Press 'ESC' to exit.")
#bot_num = input("Enter bot number : ")
host_bot=input("Enter brain block ip address : ")
while True:
    # Check if the 'up' arrow key is pressed
    if keyboard.is_pressed('up'):
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
    elif keyboard.is_pressed('l'):
        requests.get(f"http://{host_bot}/?cmd=lb_speed=180")#Left Speed
        requests.get(f"http://{host_bot}/?cmd=rb_speed=180")#Right Speed
        print("Speed set to Low")
    elif keyboard.is_pressed('m'):
        requests.get(f"http://{host_bot}/?cmd=left_speed=200")#Left Speed
        requests.get(f"http://{host_bot}/?cmd=right_speed=200")#Right Speed
        print("Speed set to Medium")
    elif keyboard.is_pressed('h'):
        requests.get(f"http://{host_bot}/?cmd=lb_speed=250")#Left Speed
        requests.get(f"http://{host_bot}/?cmd=rb_speed=250")#Right Speed
        print("Speed set to High")                    
    # Break the loop if 'ESC' is pressed to exit the program
    elif keyboard.is_pressed('esc'):
        requests.get(f"http://{host_bot}/?cmd=s")
        print("Exiting...")
        break
    else :
        requests.get(f"http://{host_bot}/?cmd=s")
