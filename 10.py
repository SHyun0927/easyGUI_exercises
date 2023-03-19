import easygui
import random


def dice_roll():
    dice = [random.randint(1, 6) for i in range(5)]
    return dice


def detect_result(dice):
    counts = [dice.count(i) for i in dice]

    if 5 in counts:
        return "Yahtzee!!"

    if 4 in counts:
        return "Four of a kind!"

    if 3 in counts:
        return "Three of a kind!"

    else:
        return "Better luck next time..."


def main():
    while True:
        player1 = easygui.enterbox("What is Player 1's name?", "Name!!")
        player2 = easygui.enterbox("What is player 2's name?", "Name!!")

        dice = dice_roll()
        for i in range(2):
            again = easygui.buttonbox(f"You rolled: {dice} \n"
                                      f"Choose: ", "Rolling...", choices=["Reroll", "Stick"])

            if again == "Reroll":
                dice = dice_roll()

            else:
                break

        easygui.msgbox(f"Your final roll is: {dice} \n"
                       f"{detect_result(dice)}", "Result!")

        restart = easygui.buttonbox("You've finished the game. Do you want to play again?", "Try?", choices=["Yes", "No"])

        if restart == "No":
            easygui.msgbox("Thank you for playing Yahtzee lite!", "Thank you!")
            break


easygui.msgbox("Welcome to Yahtzee lite!", "Welcome!")
main()
