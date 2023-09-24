import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user choice and change button color
def user_choice(choice, button):
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    
    if result == "You win!":
        global player_wins
        player_wins += 1
    elif result == "Computer wins!":
        global computer_wins
        computer_wins += 1
    
    update_score_label()
    
    # Change the button color on click
    button.config(bg='green' if result == "You win!" else 'red' if result == "Computer wins!" else 'blue')

# Function to start a new game
def start_game():
    global player_wins
    global computer_wins
    player_wins = 0
    computer_wins = 0
    update_score_label()
    # Reset button colors
    rock_button.config(bg='SystemButtonFace')
    paper_button.config(bg='SystemButtonFace')
    scissors_button.config(bg='SystemButtonFace')

# Function to end the game
def end_game():
    root.destroy()

# Function to update the score label
def update_score_label():
    score_label.config(text=f"Player Wins: {player_wins}, Computer Wins: {computer_wins}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Set window dimensions (width x height)
window_width = 400
window_height = 250
root.geometry(f"{window_width}x{window_height}")

# Create labels
label = tk.Label(root, text="Choose rock, paper, or scissors:")
label.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create buttons for user choice with padding
rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice("rock", rock_button))
paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice("paper", paper_button))
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice("scissors", scissors_button))

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Create buttons to start and end the game
start_button = tk.Button(root, text="Start Game", command=start_game)
end_button = tk.Button(root, text="End Game", command=end_game)

start_button.pack()
end_button.pack()

# Label to display the score
score_label = tk.Label(root, text="Player Wins: 0, Computer Wins: 0")
score_label.pack()

# Initialize scores
player_wins = 0
computer_wins = 0

# Run the tkinter main loop
root.mainloop()
