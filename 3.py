import easygui
import random

while True:
    weapon = ["Paper", "Scissors", "Rock"]
    bot = random.choice(weapon)
    player = easygui.buttonbox("Paper, Scissors, Rock!",
                               choices=[weapon[0], weapon[1],  weapon[2]])
    easygui.msgbox(f"You chose {player} and bot chose {bot}!", "Beating this nigga up")

    if bot == player:
        result = "Draw..."

    elif bot == "Paper" and player == "Rock" or bot == "Scissors" and player == "Paper" or bot == "Rock" and player == "Scissors":
        result = "Bot win!"

    else:
        result = "You win!"

    easygui.msgbox(f"{result}")

    play_again = easygui.buttonbox("Do you want to play again?", choices=["Yes", "No"])

    if play_again == "No":
        easygui.msgbox("Thank you for playing RPS game!")
        break




