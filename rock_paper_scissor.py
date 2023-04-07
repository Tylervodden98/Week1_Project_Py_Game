import math
import os


def write_log(win_count):
    # Check if file exists
    if os.path.isfile("./rock_paper_scissor_log.csv"):
        with open("rock_paper_scissor_log.csv", "r+") as data_num:
            data = data_num.readlines()

            # Get wins/loss data in dictionary
            wins_losses_dict = {data[i].split(":")[0]: int(data[i].split(
                ":")[1].replace("\n", "")) for i in range(0, len(data))}

            # Update dictionary
            if win_count == 0:
                # P1 Win
                wins_losses_dict["p1_game_wins"] += 1
                wins_losses_dict["p2_game_losses"] += 1
            else:
                # P2 Win
                wins_losses_dict["p2_game_wins"] += 1
                wins_losses_dict["p1_game_losses"] += 1
            # For viewing log
            # print(wins_losses_dict)
            # write dict back to file, overwrite
            data_num.truncate()
            for key, value in wins_losses_dict.items():
                data_num.write(f"{key}:{value}\n")

        with open("rock_paper_scissor_log.csv", "wt") as data_num:
            for key, value in wins_losses_dict.items():
                data_num.write(f"{key}:{value}\n")
    # iff it doesnt
    else:
        with open("rock_paper_scissor_log.csv", "wt") as num_log:
            # P1 wins
            if win_count == 0:
                log_dict = {"p1_game_wins": 1, "p1_game_losses": 0,
                            "p2_game_wins": 0, "p2_game_losses": 1}
            # P2 wins
            else:
                log_dict = {"p1_game_wins": 0, "p1_game_losses": 1,
                            "p2_game_wins": 1, "p2_game_losses": 0}
            for key, value in log_dict.items():
                num_log.write(f"{key}:{value}\n")


def r_p_s_game():
    while True:
        try:
            game = int(input("BO3 or BO5?, enter 3 or 5"))
            break
        except ValueError:
            print("Please enter 3 or 5")

    bestof = math.floor(game / 2) + 1
    p1_score = 0
    p2_score = 0
    # win count for logging
    win_count = 0
    while p1_score < bestof and p2_score < bestof:
        # Get user 1 input r,p,s
        player1 = input(
            "Player1, please enter r,p,s for Rock, Paper, or Scissors: ")
        player1 = player1.lower()
        print(player1)
        check_valid1 = False
        if player1 != "r" and player1 != "p" and player1 != "s":
            print("Please enter valid input of 'r','p' or 's'")
        else:
            check_valid1 = True

        # Get user 2 input r,p,s
        player2 = input(
            "Player 2, please enter r,p,s for Rock, Paper, or Scissors: ")
        player2 = player2.lower()
        print(player2)
        check_valid2 = False
        if player2 != "r" and player2 != "p" and player2 != "s":
            print("Please enter valid input of 'r','p' or 's'")
        else:
            check_valid2 = True

        if check_valid1 == True and check_valid2 == True:
            # Play r,p,s
            # First check if they chose the same option
            if player1 == player2:
                print(f"Both Players chose {player1}, it's a tie!")
            elif player1 == "r" and player2 == "s":
                print("Player 1 wins!")
                p1_score += 1
                game -= 1
            elif player1 == "p" and player2 == "r":
                print("Player 1 wins!")
                p1_score += 1
                game -= 1
            elif player1 == "s" and player2 == "p":
                print("Player 1 wins!")
                p1_score += 1
                game -= 1
            else:
                # All other cases P2 wins
                print("Player 2 wins!")
                p2_score += 1
                game -= 1
        else:
            if check_valid1 == False:
                print("Player 1 has an invalid input")
            else:
                print("Player 2 has an invalid input")
    else:
        if p1_score > p2_score:
            print(
                f"Player 1 wins with a score of {p1_score} to Player 2's score of {p2_score}")
            write_log(win_count)

        else:
            print(
                f"Player 2 wins with a score of {p2_score} to Player 1's score of {p1_score}")
            win_count += 1
            write_log(win_count)
