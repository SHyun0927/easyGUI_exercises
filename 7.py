# made the convertor into function
import easygui


def spelling_convertor():
    while True:
        nz_word = easygui.enterbox("Please write word in NZ spelling", "NZ word to US word converter")

        if nz_word == "":
            easygui.msgbox("Please enter a word to convert", "Error!")
            return

        if "our" in nz_word:
            us_word = nz_word.replace("our", "or")

        else:
            if "ise" in nz_word or "yse" in nz_word:
                us_word = nz_word.replace("ise", "ize").replace("yse", "yze")

            else:
                us_word = "--"
                easygui.msgbox("There are no nz word detected.")

        restart = easygui.buttonbox(f"The American spelling for {nz_word} is {us_word}. \n"
                                    f"Do you want to convert another word?", choices=["Yes", "No"])

        if restart == "No":
            break


spelling_convertor()
easygui.msgbox("Thank you for using the convertor!")
