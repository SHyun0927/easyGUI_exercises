import easygui
import random


# 주사위 5개를 숫자 1-6사이로 굴린다
def dice_roll():
    dice = [random.randint(1, 6) for i in range(5)]
    return dice


# 결과를 감지한다.
def detect_result(dice):
    # 5가지가 모두 같이 나온다면 야추
    if dice.count(dice[0]) == 5:
        return "Yahtzee!"

    # 4가지가 같이 나온다면 Four  of a kind
    # 해당 코드가 작동하는 방식은 list에서 0번(첫번쨰)칸 혹은 1번(두번쨰) 칸의 숫자를 분석하며 해당 숫자들과 같은 숫자가 있는지 찾는다.
    elif dice.count(dice[0]) == 4 or dice.count(dice[1]) == 4:
        return "Four of a kind"

    # 3가지가 같다면 나온다면 Three of kind을 출력.
    # 여기서도 1번, 2번, 혹은 3번칸을 체크하여 같은 숫자가 있는지 본다.
    elif dice.count(dice[0]) == 3 or dice.count(dice[1]) == 3 or dice.count(dice[2]) == 3:
        return "Three of a kind"

    # 만약 같은 숫자가 2개 혹은 존재하지 않는다면 이 문구를 표시한다.
    else:
        return "Better luck next time..."

# 정보) 사실 더 깔끔하게 만들수 있는 방법이 있다. 일단 이해하기 쉬우라고.


# 코드를 전부 잇는 메인루틴 function
def main():
    # while True loop를 사용하여 유저가 다시 플레이하길 원할 떄 무한적으로 반복할 수 있게 한다
    while True:
        # 주사위를 굴린다
        dice = dice_roll()
        # 이 부분은 유저가 주사위를 3(range loop에서 두번)번 다시 굴릴 수 있게 해 준다.
        for i in range(2):
            # 여기는 버튼박스를 활용하여 다시 굴릴지, 선택지에 그대로 있을지 선택한다.
            again = easygui.buttonbox(f"You rolled: {dice} \n"
                                      f"Choose: ", "Rolling...", choices=["Reroll", "Stick"])

            # 만약 다시 한다면, dice_roll() function을 가져와 다시 굴린다.
            if again == "Reroll":
                dice = dice_roll()

            # 만약 원하지 않는다면 해당 loop를 break한다.
            else:
                break

        # 결과 (선택한 주사위 및 결과(야추, Four/Three of a kind)를 출력)
        easygui.msgbox(f"Your final roll is: {dice} \n"
                       f"{detect_result(dice)}", "Result!")\

        # 유저가 3개의 턴을 전부 행하면, 다시 플레이하고 싶은지 물어본다.
        restart = easygui.buttonbox("You've had 3 turns. Do you want to play again?", "Try?", choices=["Yes", "No"])

        # 만약 아니라고 대답한다면, 종료 인사를 표시한 뒤 while loop을 break한다.
        if restart == "No":
            easygui.msgbox("Thank you for playing Yahtzee lite!", "Thank you!")
            break




# 메인 루틴
main()
