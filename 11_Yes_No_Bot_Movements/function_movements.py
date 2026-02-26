import requests

host_bot=input("Enter brain block ip address : ")
def yes():
    requests.get(f"http://{host_bot}/?cmd=f(500)")
    
def no():
    requests.get(f"http://{host_bot}/?cmd=b(500)")
a_1=input("Is the sky blue ? y or n : ")

if a_1=="y":
    print("Correct Answer")
    yes()
else:
    print("Wrong Answer")
    no()



a_2=input("Does sun rises in west ? y or n : ")

if a_2=="n":
    print("Correct Answer")
    yes()
else:
    print("Wrong Answer")
    no()


a_3=input("Does tiger eats grass ? y or n : ")

if a_3=="n":
    print("Correct Answer")
    yes()
else:
    print("Wrong Answer")
    no()
    

    
          
