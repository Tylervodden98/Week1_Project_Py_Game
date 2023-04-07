from number_guess_game import play_number_guess
from rock_paper_scissor import r_p_s_game
from tictactoe import play_t3
import tkinter as tk

window = tk.Tk()
window.geometry("250x200")
window.title("Game Manager")

# Label
label = tk.Label(text="Select a Game to Play")

l1 = tk.Label(window, text="What game would you like to play?")
l1.grid(row=0, column=2, sticky="n")

# Button modifiers


def button1_click():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    play_number_guess()
    button1.configure(state="normal")
    button2.configure(state="normal")
    button3.configure(state="normal")
    print("Try picking another game to play!")


def button2_click():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    r_p_s_game()
    button1.configure(state="normal")
    button2.configure(state="normal")
    button3.configure(state="normal")
    print("Try picking another game to play!")


def button3_click():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    play_t3()
    button1.configure(state="normal")
    button2.configure(state="normal")
    button3.configure(state="normal")
    print("Try picking another game to play!")


# Buttons
button1 = tk.Button(text="Number Guess Game", command=button1_click)
button1.grid(row=1, column=2, sticky="news")
button2 = tk.Button(text="Rock Paper Scissors", command=button2_click)
button2.grid(row=2, column=2, sticky="news")
button3 = tk.Button(text="TicTacToe", command=button3_click)
button3.grid(row=3, column=2, sticky="news")


window.mainloop()
# play_number_guess()

# r_p_s_game()

# play_t3()
