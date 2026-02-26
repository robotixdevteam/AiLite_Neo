import tkinter as tk
import random
import requests
import http.client
import time

host=input("Enter brain block ip address : ")
print("Bot Action : Stone - Forward |Paper - Backward | Scissors - Right")
port = 80

def send_re_httpquest(host, port, path):
    """Send HTTP request with retries."""
    retries = 10  # Number of retries
    for _ in range(retries):
        conn = None
        try:
            conn = http.client.HTTPConnection(, port)
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

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'stone' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'stone') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        #requests.get(f"http://{host}/?cmd=f(1000)")
        return "You win!"
    else:
        #requests.get(f"http://{host}/?cmd=b(1000)")
        return "Computer wins!"

def play_game(choice):
    global player_wins
    computer_choice = random.choice(['stone', 'paper', 'scissors'])
    result = determine_winner(choice, computer_choice)
    
    # Update the result_label with both the computer's choice and the result
    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")
    if computer_choice =="stone":
       requests.get(f"http://{host}/?cmd=r(1500)")
    elif computer_choice =="paper":
       requests.get(f"http://{host}/?cmd=f(1000)")
    elif computer_choice =="scissors":
       path=f"/?cmd=l(800)"
       send_re_httpquest(host, port, path)
       path=f"/?cmd=f(800)"
       send_re_httpquest(host, port, path)
       path=f"/?cmd=r(800)"
       send_re_httpquest(host, port, path)
       path=f"/?cmd=f(1200)"
       send_re_httpquest(host, port, path)
       path=f"/?cmd=l(800)"
       send_re_httpquest(host, port, path)               
    # Highlight the button representing computer's choice
    if computer_choice == 'stone':
        stone_button.config(bg='blue')
        paper_button.config(bg='SystemButtonFace')  # Reset other buttons' color
        scissors_button.config(bg='SystemButtonFace')  # Reset other buttons' color
    elif computer_choice == 'paper':
        paper_button.config(bg='blue')
        stone_button.config(bg='SystemButtonFace')  # Reset other buttons' color
        scissors_button.config(bg='SystemButtonFace')  # Reset other buttons' color
    elif computer_choice == 'scissors':
        scissors_button.config(bg='blue')
        stone_button.config(bg='SystemButtonFace')  # Reset other buttons' color
        paper_button.config(bg='SystemButtonFace')  # Reset other buttons' color
    
    if result == "You win!":
        player_wins += 1
        if player_wins == 3:
            root.destroy()

root = tk.Tk()
root.title("Stone Paper Scissors")

choices = ['stone', 'paper', 'scissors']
player_wins = 0

stone_button = tk.Button(root, text="Stone", command=lambda: play_game('stone'))
stone_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))
scissors_button.pack()

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack()

root.mainloop()
