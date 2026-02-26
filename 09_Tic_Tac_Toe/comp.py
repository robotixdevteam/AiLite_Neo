import tkinter as tk
import random
import requests

host_bot=input("Enter brain block ip address : ")

print("RULES : ")
print("Level 1 : Win - Forward | Lose - Rotate | Tie - Left")
print("Level 2 : Win - Forward | Lose - Backward | Tie - Left")
print("Level 3 : Win - Forward & Rotate | Lose - Backward | Tie - Forward")

def tic_tac_toe_gui():
    def check_winner(b, player):
        # Check rows, columns, and diagonals
        return any(all(cell == player for cell in row) for row in b) or \
               any(all(b[row][col] == player for row in range(3)) for col in range(3)) or \
               all(b[i][i] == player for i in range(3)) or \
               all(b[i][2-i] == player for i in range(3))

    def get_empty_positions(b):
        return [(row, col) for row in range(3) for col in range(3) if b[row][col] == " "]

    def computer_move(b):
        empty_positions = get_empty_positions(b)
        return random.choice(empty_positions)

    def cell_clicked(row, col):
        nonlocal current_player, game_winner
        if board[row][col] == " ":
            board[row][col] = current_player
            buttons[row][col].config(text=current_player)
            if check_winner(board, current_player):
                result_label.config(text=f"Player {current_player} wins!")
                game_winner = current_player  # Store the winner
                disable_buttons()
            elif not any(" " in row for row in board):
                result_label.config(text="It's a tie!")
                disable_buttons()
            else:
                current_player = 'X' if current_player == 'O' else 'O'
                if current_player == 'O':
                    r, c = computer_move(board)
                    cell_clicked(r, c)

    def disable_buttons():
        for row in buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def create_board_gui(root):
        nonlocal buttons
        buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(root, text=" ", font=('Arial', 20), width=4, height=2,
                                   command=lambda r=row, c=col: cell_clicked(r, c))
                button.grid(row=row, column=col, sticky="nsew")
                button_row.append(button)
            buttons.append(button_row)

    # Main GUI Setup
    root = tk.Tk()
    root.title("Tic Tac Toe")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Player 'X' always starts first
    game_winner = None  # Variable to store the winner
    buttons = []

    create_board_gui(root)
    result_label = tk.Label(root, text="", font=('Arial', 14))
    result_label.grid(row=3, columnspan=3)
    
    root.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    if game_winner =="X":
        print(f"The game was won by {game_winner}.Next Round")
        requests.get(f"http://{host_bot}/?cmd=f(1000)")
        def check_winner(board, player):
            # Check rows
            for row in board:
                if all(cell == player for cell in row):
                    return True
            # Check columns
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2-i] == player for i in range(3)):
                return True
            return False

        def get_empty_positions(board):
            return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

        def computer_move(board):
            empty_positions = get_empty_positions(board)
            return random.choice(empty_positions)

        def cell_clicked(row, col):
            nonlocal current_player, board, winner
            if board[row][col] == " " and winner is None:
                board[row][col] = current_player
                buttons[row][col].config(text=current_player)
                if check_winner(board, current_player):
                    winner = current_player
                    result_label.config(text=f"Player {current_player} wins!")
                    disable_buttons()
                elif all(all(cell != " " for cell in row) for row in board):
                    result_label.config(text="It's a tie!")
                    disable_buttons()
                else:
                    switch_player()

        def switch_player():
            nonlocal current_player
            current_player = 'X' if current_player == 'O' else 'O'
            if current_player == 'O':
                row, col = computer_move(board)
                cell_clicked(row, col)

        def disable_buttons():
            for row in range(3):
                for col in range(3):
                    buttons[row][col].config(state=tk.DISABLED)

        def create_board_gui(root):
            nonlocal buttons
            buttons = []
            for row in range(3):
                button_row = []
                for col in range(3):
                    button = tk.Button(root, text=" ", font=('Arial', 20), width=4, height=2,
                                    command=lambda r=row, c=col: cell_clicked(r, c))
                    button.grid(row=row, column=col, sticky="nsew")
                    button_row.append(button)
                buttons.append(button_row)

        # Main GUI Setup
        root = tk.Tk()
        root.title("Tic Tac Toe")
        
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = 'O'  # Computer starts first
        winner = None
        buttons = []

        create_board_gui(root)
        result_label = tk.Label(root, text="Computer's turn", font=('Arial', 14))
        result_label.grid(row=3, columnspan=3)

        # Start with a computer move if the computer starts first
        if current_player == 'O':
            row, col = computer_move(board)
            cell_clicked(row, col)

        root.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------    
        if winner =="X":
            print(f"The game was won by {winner}.Final Round")
            requests.get(f"http://{host_bot}/?cmd=f(1000)")

            def check_winner(b, player):
                # Check rows, columns, and diagonals
                return any(all(cell == player for cell in row) for row in b) or \
                    any(all(b[row][col] == player for row in range(3)) for col in range(3)) or \
                    all(b[i][i] == player for i in range(3)) or \
                    all(b[i][2-i] == player for i in range(3))

            def get_empty_positions(b):
                return [(row, col) for row in range(3) for col in range(3) if b[row][col] == " "]

            def minimax(b, depth, is_maximizing):
                if check_winner(b, 'X'):
                    return {'score': -1}
                elif check_winner(b, 'O'):
                    return {'score': 1}
                elif not get_empty_positions(b):
                    return {'score': 0}

                if is_maximizing:
                    best_score = float('-inf')
                    best_move = None
                    for (row, col) in get_empty_positions(b):
                        b[row][col] = 'O'
                        score = minimax(b, depth - 1, False)['score']
                        b[row][col] = ' '
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
                    return {'score': best_score, 'position': best_move}
                else:
                    best_score = float('inf')
                    best_move = None
                    for (row, col) in get_empty_positions(b):
                        b[row][col] = 'X'
                        score = minimax(b, depth - 1, True)['score']
                        b[row][col] = ' '
                        if score < best_score:
                            best_score = score
                            best_move = (row, col)
                    return {'score': best_score, 'position': best_move}

            def computer_move(b):
                if len(get_empty_positions(b)) == 9:
                    return random.choice(get_empty_positions(b))
                return minimax(b, 0, True)['position']

            def cell_clicked(row, col):
                nonlocal current_player, board, final_winner
                if board[row][col] == " " and current_player == 'X':
                    board[row][col] = current_player
                    buttons[row][col].config(text=current_player)
                    if check_winner(board, current_player):
                        final_winner = current_player
                        result_label.config(text=f"Player {current_player} wins!")
                        disable_buttons()
                    elif not get_empty_positions(board):
                        result_label.config(text="It's a tie!")
                        disable_buttons()
                    else:
                        current_player = 'O'
                        row, col = computer_move(board)
                        board[row][col] = 'O'
                        buttons[row][col].config(text='O')
                        if check_winner(board, 'O'):
                            final_winner = 'O'
                            result_label.config(text="Player O wins!")
                            disable_buttons()
                        elif not get_empty_positions(board):
                            result_label.config(text="It's a tie!")
                            disable_buttons()
                        current_player = 'X'

            def disable_buttons():
                for row in range(3):
                    for col in range(3):
                        buttons[row][col].config(state=tk.DISABLED)

            def create_board_gui(root):
                nonlocal buttons
                buttons = []
                for row in range(3):
                    button_row = []
                    for col in range(3):
                        button = tk.Button(root, text=" ", font=('Arial', 20), width=4, height=2,
                                        command=lambda r=row, c=col: cell_clicked(r, c))
                        button.grid(row=row, column=col, sticky="nsew")
                        button_row.append(button)
                    buttons.append(button_row)

            # Main GUI Setup
            root = tk.Tk()
            root.title("Tic Tac Toe")
            
            board = [[" " for _ in range(3)] for _ in range(3)]
            current_player = 'X'
            buttons = []
            final_winner = None

            create_board_gui(root)
            result_label = tk.Label(root, text="Player X's turn", font=('Arial', 14))
            result_label.grid(row=3, columnspan=3)

            root.mainloop()
            if final_winner =="X":
               print(f"Hurry u have successfully completed all the rounds {final_winner}.")
               requests.get(f"http://{host_bot}/?cmd=f(1000)")
               requests.get(f"http://{host_bot}/?cmd=r(1000)")
            elif final_winner =="O":
               print(f"The game was won by {final_winner}.Better Luck Next Time")
               requests.get(f"http://{host_bot}/?cmd=b(2000)") 
            else:
               print("The game ended in a tie ")
               requests.get(f"http://{host_bot}/?cmd=f(1000)")      
        elif winner =="O":
               print(f"The game was won by {winner}.Better Luck Next Time")
               requests.get(f"http://{host_bot}/?cmd=b(1000)") 
        else:
            print("The game ended in a tie ")
            requests.get(f"http://{host_bot}/?cmd=l(500)") 
    elif game_winner =="O":
               print(f"The game was won by {game_winner}.Better Luck Next Time")
               requests.get(f"http://{host_bot}/?cmd=r(1500)") 
    else:
        print("The game ended in a tie ")
        requests.get(f"http://{host_bot}/?cmd=l(500)") 

if __name__ == "__main__":
    tic_tac_toe_gui()
