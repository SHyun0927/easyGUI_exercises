import easygui

# dictionary는 어떤 방식으로 저장하던 상관 없는데... 난 세로로 정렬 안했음.
combo = {
    "VALUE": {"items": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}},
    "CHEEZY": {"items": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}},
    "SUPER": {"items": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}
}


# 콤보 추가 function
def add_combo():
    # 콤보 이름을 정한다. .upper() 구문은 있어도 되고 없어도 됨 난 통일성을 위해 그냥 썼음.
    combo_name = easygui.enterbox("Enter the name of the combo", "New combo!").upper()
    # combo_name이란 dictoinary를 생성 후 그 안에 "items" 라는 dictonary를 또 생성
    combo[combo_name] = {"items": {}}

    for i in range(3):
        if i == 0:
            order = "burger"
        elif i == 1:
            order = "side menu"
        else:
            order = "drink"

        # 콤보 아이템과 가격을 물어보는 코드. 가격에서 enterbox를 사용하면서 float를 사용해야 소숫점도 나타낼수 있다.
        combo_item = easygui.enterbox(f"Enter name of the {order} to add to the combo:")
        # 만약 여기서 integerbox를 쓴다면 소숫점 사용 불가.
        price = float(easygui.enterbox(f'Enter the price of {combo_item}:'))
        # combo_item에서 얻는 이름과 가격을 dictonary에 넣는 코드이다.
        combo[combo_name]["items"][combo_item] = price


# 내용물을 보여주는 function
def display_combo():
    # 첫 메시지
    msg = "List of combos:\n"
    # item = combo 종류
    # 이 부분이 왜 이런지 모르겠다면 onenote 'introduction to dictonary' page 9 확인 부탁
    for item in combo:
        # 콤보 이름을 불러온다
        msg += f"{item} \n"
        # 콤보 안애 아이템마다:
        for dishes in combo[item]["items"]:
            # 아이템 + 가격(소숫점 2자리)를 보여준다.
            # 참고: ""(쌍따옴표) 가 아니라 ''(따옴표)를 써야 가격을 불러올수 있다. 왠진모름;
            msg += f'   {dishes} ${float(combo[item]["items"][dishes]):.2f} \n'

    # 그리고 추가했던 msg를 텍스트로 불러온다.
    easygui.msgbox(msg, title="Menus")


add_combo()
display_combo()
