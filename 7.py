import easygui


def spelling_convertor():
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
            easygui.msgbox("There are no nz word detected.")
            return

    easygui.msgbox(f"The American spelling for {nz_word} is {us_word}")


spelling_convertor()
