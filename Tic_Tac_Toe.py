import random


def board_design(marker_input):
    print("\n"*100)
    print(" | " + marker_input[1] + " | " + marker_input[2] + " | " + marker_input[3] + " | ")
    print(" |" + "---" + "|" + "---" + "|" + "---" + "|")
    print(" | " + marker_input[4] + " | " + marker_input[5] + " | " + marker_input[6] + " | ")
    print(" |" + "---" + "|" + "---" + "|" + "---" + "|")
    print(" | " + marker_input[7] + " | " + marker_input[8] + " | " + marker_input[9] + " | ")

def player_marker():
    marker = ''
    while not (marker == 'x' or marker == 'o'):
        marker = input("choose your marker,(X or O): ").lower()
    if marker == 'x':
        return ('X','O')
    else:
        return ('O','X')


def marker_position(marker_input, marker, position):
    marker_input[position] = marker


def win_check(marker_input, mark):
    return ((marker_input[7] == mark and marker_input[8] == mark and marker_input[9] == mark) or  # across the top
            (marker_input[4] == mark and marker_input[5] == mark and marker_input[6] == mark) or  # across the middle
            (marker_input[1] == mark and marker_input[2] == mark and marker_input[3] == mark) or  # across the bottom
            (marker_input[7] == mark and marker_input[4] == mark and marker_input[1] == mark) or  # down the middle
            (marker_input[8] == mark and marker_input[5] == mark and marker_input[2] == mark) or  # down the middle
            (marker_input[9] == mark and marker_input[6] == mark and marker_input[3] == mark) or  # down the right side
            (marker_input[7] == mark and marker_input[5] == mark and marker_input[3] == mark) or  # diagonal
            (marker_input[9] == mark and marker_input[5] == mark and marker_input[1] == mark))  # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            print(f'player {turn}')
            board_design(theBoard)
            position = player_choice(theBoard)
            marker_position(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                board_design(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    board_design(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            board_design(theBoard)
            position = player_choice(theBoard)
            marker_position(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                board_design(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    board_design(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break