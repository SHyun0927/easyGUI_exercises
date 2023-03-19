import easygui
import random


def dice_roll():
    dice = [random.randint(1, 6) for i in range(5)]
    return dice


def detect_result(dice):
    find_number = [dice.count(i) for i in dice]

    if 5 in find_number:
        return "Yahtzee!!", 50

    if 4 in find_number:
        return "Four of a kind!", 30

    if 3 in find_number:
        return "Three of a kind!", 10

    else:
        return "Better luck next time...", 0


def play_game(player):
    dice = dice_roll()

    for i in range(2):
        again = easygui.buttonbox(f"{player}'s roll is: {dice} \n"
                                  f"Choose: ", "Rolling...", choices=["Reroll", "Stick"])

        if again == "Reroll":
            dice = dice_roll()

        else:
            break

    result, score = detect_result(dice)
    easygui.msgbox(f"{player}'s your final roll is: {dice} \n"
                   f"{result}\n"
                   f"You scored {score} points!", "Result!")
    return score


def main():
    easygui.msgbox("Welcome to Yahtzee lite!", "Welcome!")

    while True:

        player1 = easygui.enterbox("What is Player 1's name?", "Name!!")
        player2 = easygui.enterbox("What is player 2's name?", "Name!!")

        score1 = play_game(player1)
        score2 = play_game(player2)

        if score1 > score2:
            easygui.msgbox(f"{player1} wins with {score1} points!", "Player 1 wins!")

        elif score1 < score2:
            easygui.msgbox(f"{player2} wins with {score2} points!", "Player 2 wins!")

        else:
            easygui.msgbox("It's a draw!", "Draw...")

        restart = easygui.buttonbox("You've finished the game. Do you want to play again?", "Try?", choices=["Yes", "No"])

        if restart == "No":
            easygui.msgbox("Thank you for playing Yahtzee lite!", "Thank you!")
            break


main()
