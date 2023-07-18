def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(square != ' ' for row in board for square in row)

def get_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Please enter a valid row and column (0, 1, or 2).")
        except ValueError:
            print("Invalid input. Please enter a valid row and column (0, 1, or 2).")

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    while True:
        print_board(board)
        player = players[turn]
        print(f"Player {player}'s turn.")

        row, col = get_move()

        if board[row][col] == ' ':
            board[row][col] = player

            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            turn = 1 - turn
        else:
            print("That square is already taken. Please choose another.")

if __name__ == "__main__":
    play_tic_tac_toe()
