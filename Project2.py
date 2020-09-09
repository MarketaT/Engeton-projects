def welcoming():
    print("WELCOME TO TIC TAC TOE")
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid")
    print("The WINNER is who succeeds in placing three of their marks in a")
    print("* horizontal,\n* vertical or\n* diagonal row\nLet's start the game")

def creating_board():
    list1 = list(range(1,3**2+1))
    list2 = [' ']*3**2
    board = dict(zip(list1,list2))
    return board

def print_board(board):
    x = 6*'-'
    print(x)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(x)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(x)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(x)

def win_horizontal(board):
    we_have_winner = False
    if board[1] == board[2] == board[3] != ' ' \
            or board[4] == board[5] == board[6] != ' ' \
            or board[7] == board[8] == board[9] != ' ':
        we_have_winner = True
    return we_have_winner

def win_vertical(board):
    we_have_winner = False
    if board[1] == board[4] == board[7] != ' '\
            or board[2] == board[5] == board[8] != ' '\
            or board[3] == board[6] == board[9] != ' ':
        we_have_winner = True
    return we_have_winner

def win_cross(board):
    we_have_winner = False
    if board[1] == board[5] == board[9] != ' '\
            or board[3] == board[5] == board[7] != ' ':
        we_have_winner = True
    return we_have_winner

def switch_players(whose_turn):
    if whose_turn == "O":
        whose_turn = "X"
    else:
        whose_turn = "O"
    return whose_turn

def no_winner(board):
    if ' ' not in board.values():
        return True
    else:
        return False

def main():
    welcoming()
    board = creating_board()
    print_board(board)
    print("========================================")
    end = False
    whose_turn = "O"

    while not end: # pojedou maximalne 9 kol
        game = int(input("Player {} Please enter your move number: ".format(whose_turn)))
        if board[game] == ' ':
            board[game] = whose_turn
        else:
            continue
        print_board(board)

        x = win_horizontal(board)
        y = win_vertical(board)
        z = win_cross(board)
        w = no_winner(board)

        if x or y or z:
            print("Congratulations, the player {} WON!".format(whose_turn))
            end = True
        elif w:
            break
        else:
            whose_turn = switch_players(whose_turn)
if __name__ == "__main__":
    main()