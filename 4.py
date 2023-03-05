import easygui

school = easygui.enterbox("Enter the name of the school", "School name")

max_class_size = easygui.integerbox("What is the maximum number of children allowed per class: \n"
                                    "It must be a number between 10 and 30", "Maximum school size",
                                    upperbound=30, lowerbound=10)

total_roll = easygui.integerbox(f"What is the total of the children at {school}: \n"
                                f"it must be number between 10 and 1400", "Total roll of the school",
                                upperbound=1400, lowerbound=10)

required_teacher = total_roll // max_class_size

teachers_present = easygui.integerbox(f"How many teachers at {school} \n"
                                      f"Must be a number between 1 and 120", "Actual number of teachers",
                                      upperbound=120, lowerbound=1)

if teachers_present > required_teacher:
    easygui.msgbox(f"You have too many teachers. \n"
                   f"You could do it without {teachers_present - required_teacher} teacher/s", "Over-Staffed!!")

elif teachers_present < required_teacher:
    easygui.msgbox(f"You need more teachers. \n"
                   f"You will need {required_teacher - teachers_present} teacher/s.", "Low-Staffed!!")

else:
    easygui.msgbox()

easygui.msgbox("Thank you for using this teacher calculator!", "Goodbye!")
