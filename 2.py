import random
import easygui

player = 0

for roll in range(2):
    player += 1
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    easygui.msgbox(f"Player {player} you rolled: \n \n {die1} and {die2} \n \n"
                   f"Total: {die1 + die2}", f"Player {player} rolled")
