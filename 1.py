import easygui, random

for i in range(5):
    alphabet = "elephant"
    user_alphabet = random.choice(alphabet)
    easygui.msgbox(msg=user_alphabet, title=f"Letter {i+1} chosen")

