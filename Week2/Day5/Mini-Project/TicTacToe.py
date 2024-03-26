# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. 
# You can implement many more helper functions or choose a completely different appoach if you want.

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to get the position from the player
def player_input(player):
    while True:
        position = input(f"Player {player}, enter your position (row,col): ")
        try:
            row, col = map(int, position.split(","))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "-":
                return row, col
            else:
                print("Invalid position. Please try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by comma.")

# Function to check whether there is a winner or not
def check_win(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True
    return False

# Main function to play the game
def play():
    board = [["-" for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        display_board(board)
        row, col = player_input(player)
        board[row][col] = player
        if check_win(board):
            display_board(board)
            print(f"Player {player} wins!")
            break
        if all(board[i][j] != "-" for i in range(3) for j in range(3)):
            display_board(board)
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"

# Play the game
play()


    
    