import random
import json
import os


def write_log(win_count):
    # Check if file exists
    if os.path.isfile("./number_guess_log.csv"):
        with open("number_guess_log.csv", "r+") as data_num:
            data = data_num.readlines()

            # Get wins/loss data in dictionary
            wins_losses_dict = {data[i].split(":")[0]: int(data[i].split(
                ":")[1].replace("\n", "")) for i in range(0, len(data))}

            # Update dictionary
            if win_count == 0:
                # Loss
                wins_losses_dict["game_losses"] += 1
            else:
                # Win
                wins_losses_dict["game_wins"] += 1

            # write dict back to file, overwrite
            data_num.truncate()
            for key, value in wins_losses_dict.items():
                data_num.write(f"{key}:{value}\n")
            # for testing
            # print(wins_losses_dict)
        with open("number_guess_log.csv", "wt") as data_num:
            for key, value in wins_losses_dict.items():
                data_num.write(f"{key}:{value}\n")
    # iff it doesnt
    else:
        with open("number_guess_log.csv", "wt") as num_log:
            # loss
            if win_count == 0:
                log_dict = {"game_wins": 0, "game_losses": 1}
            # win
            else:
                log_dict = {"game_wins": 1, "game_losses": 0}
            for key, value in log_dict.items():
                num_log.write(f"{key}:{value}\n")


def play_number_guess():
    rand_lower = random.randint(0, 81)
    while True:
        rand_upper = random.randint(rand_lower, 100)
        # iff upper range within 20 randomize again
        if rand_upper - 20 < rand_lower:
            rand_upper = random.randint(rand_lower, 100)
        else:
            break

    rand_select = random.randrange(rand_lower, rand_upper)

    win_count = 0
    guesses = 5

    print(f"Please select a number between {rand_lower} and {rand_upper}.")

    # Add more guess features?
    game_over = False
    while not game_over:

        while True:
            try:
                guess = int(input("Please enter your guess: "))
                break
            except ValueError:
                print("Please enter an integer")

        if guess == rand_select:
            print("You win!!! Congrats!")
            win_count += 1
            game_over = True
            write_log(win_count)
        elif guess > rand_select:
            guesses -= 1
            if guesses == 0:
                print("You stink! Get better at guessing numbers.")
                game_over = True
                write_log(win_count)
            print(f"Too high try again! {guesses} guesses left!")
        elif guess < rand_select:
            guesses -= 1
            if guesses == 0:
                print("You stink! Get better at guessing numbers.")
                game_over = True
                write_log(win_count)
            print(f"Too low try again! {guesses} guesses left!")
