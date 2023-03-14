import easygui
dice = [1, 1, 1, 1, 1]

counts = [dice.count(5) for i in range(1, 7)]

if 5 in counts:
    easygui.msgbox("sex")
