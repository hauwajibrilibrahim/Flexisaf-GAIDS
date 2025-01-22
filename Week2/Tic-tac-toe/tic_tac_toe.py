board = [" " for _ in range(9)]  # A single list for 3x3 board

# Print the game board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

# Check if there's a winner
def check_winner(player):
    # Winning combinations: rows, columns, and diagonals
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Check if the board is full
def is_tie():
    return " " not in board

# AI move: pick the first empty cell
def ai_move():
    for i in range(9):
        if board[i] == " ":
            return i

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player's turn
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Cell already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 0 and 8.")
            continue

        board[move] = "X"
        print_board()

        # Check if player wins or game is a tie
        if check_winner("X"):
            print("You win!")
            break
        if is_tie():
            print("It's a tie!")
            break

        # AI's turn
        ai_move_index = ai_move()
        board[ai_move_index] = "O"
        print("AI played:")
        print_board()

        # Check if AI wins or game is a tie
        if check_winner("O"):
            print("AI wins!")
            break
        if is_tie():
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
