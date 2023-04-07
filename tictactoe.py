import os
BOARD = {1: ' ',  2: ' ',  3: ' ',

         4: ' ',  5: ' ',  6: ' ',

         7: ' ',  8: ' ',  9: ' '}


def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------
    count = 0
    board_values = list(BOARD.values())
    for num in range(0, 9, 3):
        print(
            f'| {board_values[num]} | {board_values[num +1]} | {board_values[num+2]} |')


def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------
    while True:
        try:
            space = int(input(
                f"Player {player}, Please enter the space number between 1-9 where you would like to place your input: "))
            # Check if number input is between range, and space is empty
            if 1 <= space <= 9:
                if BOARD[space] == " ":
                    return space
                else:
                    print(
                        f"Board space of {space} is not empty, try another one!")
            else:
                print("Integer must be between 1-9!")
        except ValueError:
            print("Please try again, input is not an Integer")
        except TypeError:
            print("Please try again, input is not an Integer")


def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------
    print(
        f"Congrats Player {player}!!! You win!!! This is how your board ended: ")
    render()


def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------
    # Horizontal Win

    if BOARD[1] == BOARD[2] == BOARD[3] != " " or BOARD[4] == BOARD[5] == BOARD[6] != " " or BOARD[7] == BOARD[8] == BOARD[9] != " ":
        victory_message(player)
        write_log(player)
        return True
    # Vertical Win
    elif BOARD[1] == BOARD[4] == BOARD[7] != " " or BOARD[2] == BOARD[5] == BOARD[8] != " " or BOARD[3] == BOARD[6] == BOARD[9] != " ":
        victory_message(player)
        write_log(player)
        return True
    # Diagonal Win
    elif BOARD[1] == BOARD[5] == BOARD[9] != " " or BOARD[3] == BOARD[5] == BOARD[7] != " ":
        victory_message(player)
        write_log(player)
        return True
    else:
        return False


def write_log(player):
    # Check if file exists
    if os.path.isfile("./tic_tac_toe.csv"):
        with open("tic_tac_toe.csv", "r+") as data_num:
            data = data_num.readlines()

            # Get wins/loss data in dictionary
            wins_losses_dict = {data[i].split(":")[0]: int(data[i].split(
                ":")[1].replace("\n", "")) for i in range(0, len(data))}

            # Update dictionary
            # iff player X won
            if player == 'X':
                # X Win
                wins_losses_dict["x_game_wins"] += 1
                wins_losses_dict["y_game_losses"] += 1
            elif player == 'Y':
                # Y Win
                wins_losses_dict["y_game_wins"] += 1
                wins_losses_dict["x_game_losses"] += 1
            else:
                # For Ties
                wins_losses_dict["game_ties"] += 1

            # For viewing log
            # print(wins_losses_dict)

            # write dict back to file, overwrite
            data_num.truncate()
            for key, value in wins_losses_dict.items():
                data_num.write(f"{key}:{value}\n")

        with open("tic_tac_toe.csv", "wt") as data_num:
            for key, value in wins_losses_dict.items():
                data_num.write(f"{key}:{value}\n")
    # iff it doesnt
    else:
        with open("tic_tac_toe.csv", "wt") as num_log:
            # check player if X they won
            if player == 'X':
                log_dict = {"x_game_wins": 1, "x_game_losses": 0,
                            "y_game_wins": 0, "y_game_losses": 1, "game_ties": 0}
            # player Y won
            elif player == 'Y':
                log_dict = {"x_game_wins": 0, "x_game_losses": 1,
                            "y_game_wins": 1, "y_game_losses": 0, "game_ties": 0}
            else:
                log_dict = {"x_game_wins": 0, "x_game_losses": 0,
                            "y_game_wins": 0, "y_game_losses": 0, "game_ties": 1}
            for key, value in log_dict.items():
                num_log.write(f"{key}:{value}\n")
    pass


def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    player = 'X'
    game_round = 0
    game_over = False

    while not game_over:

        # Delete this line when you're ready to run the loop.

        # Print the current state of the board
        render()
        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(player)
        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
        BOARD[action] = player
        # Increment the game round by 1.
        game_round += 1
        print(game_round)

        # Check if the game is winnable (game_round >= 4),
        # then check for win conditions (check_win(player)),
        # and if there's a win, end the game (game_over = True),
        # and break the loop (break).
        if game_round >= 4:
            if check_win(player):
                game_over = True
        # Check if there are any open spots left (game_round == 9),
        # and if there aren't, print a tie message,
        # end the game,
        # and break the loop.
        if game_round == 9:
            print("Game is a tie, nobody won.. Get better next time.")
            # For logging a tie
            write_log("Z")
            # Clear board for next gamer from Main
            for key in BOARD.keys():
                BOARD[key] = " "
            break
        # switch players with a quick conditional loop.
        if game_round % 2 == 0:
            player = 'X'
        else:
            player = 'O'

    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
    else:
        while True:
            restart = input("Would you like to play again? Y or N?").upper()
            if restart == "Y":
                # Restart the game
                # Clear the Board
                for key in BOARD.keys():
                    BOARD[key] = " "
                # Call the function again to reset the game
                play_t3()
            elif restart == "N":
                print("See you next time!")
                # Clear board because Main() might call again
                for key in BOARD.keys():
                    BOARD[key] = " "
                break
            else:
                # Catch error
                print("Please enter a valid answer, either Y or N")

        # and reinitiate the game loop (play_t3()).
