print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


def ask_left_or_right():
    left_or_right = input(
        "To start your adventure, you have to choose which direction to go. Go Left or Right?\n").lower()
    return left_or_right


def ask_swim_or_wait():
    swim_or_wait = input(
        "You reach this mysterious island. You come upon a dock in a river. Going around would take too long.You could swim accross, or wait for a chance that a boat might dock. Swim or wait?\n").lower()
    return swim_or_wait


def ask_which_door():
    which_door = input(
        "You come upon the main hall of the castle with 3 colored doors. Which door should you choose? Red, Blue, or Yellow?\n").lower()
    return which_door


def get_left():
    return "You found an explorer preparing for an expedition. The captain agrees to take you on the expedition as a crew member"


def get_right():
    return "You asked a group of sailors if you can join their crew. Unfortunately, these sailors are actually pirates! You were robbed and forced to be their servant"


def get_left_or_right_else():
    return "You did not choose left or right. Unfortunately this proved disastrous. You were trampled by a horse stampede"


def get_wait():
    return "Patience is truly a virtue. a canoe docked and an old man agreed to take you across the river toward the castle"


def get_swim():
    return "Impatience proved unwise. In the middle of crossing a river, the current carried you farther away until you were adrift in the sea & eaten by a shark"


def get_swim_or_wait_else():
    return "So you did not choose to swim or wait. You wander around the island and was spotted and captured by local raiders!"


def get_red_door():
    return "Upon opening the red door, you see a fire breathing dragon that immediately engulfs you in flames!"


def get_blue_door():
    return "Upon opening a blue door, a torrent rushed out and filled the main hall, drowning you in the procees!"


def get_yellow_door():
    return "Upon opening the yellow door, you see a vast amount of treasure filled the room you enter. You have accomplished your mission & you live happily ever after!"


def get_door_else():
    return "Instead of choosing the door, you rest in the great hall. While resting, A massive troll enters the main hall. Apparently they are the owners of the castle. Seeing you rest angered the troll who then proceeded to feast on you!"


def main():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure")

    # left_or_right = ask_left_or_right()

    # if left_or_right == "Left".lower():
    #     get_left()
    #     swim_or_wait = ask_swim_or_wait()
    #     if swim_or_wait == "Wait".lower():
    #         get_wait()
    #         which_door = ask_which_door()
    #         if which_door == "Yellow".lower():
    #             print(get_yellow_door())
    #         elif which_door == "Red".lower():
    #             print(get_red_door())
    #         elif which_door == "Blue".lower():
    #             print(get_blue_door())
    #         else:
    #             print(get_door_else())
    #     elif swim_or_wait == "Swim".lower():
    #         print(get_swim())
    #     else:
    #         print(get_swim_or_wait_else())
    # elif left_or_right == "Right".lower():
    #     print(get_right())
    # else:
    #     print(get_left_or_right_else())

    left_or_right = ask_left_or_right()

    if left_or_right == "Left":
        get_left()
        swim_or_wait = ask_swim_or_wait()
        if swim_or_wait == "Wait":
            get_wait()
            which_door = ask_which_door()
            if which_door == "Yellow":
                print(get_yellow_door())
            elif which_door == "Red":
                print(get_red_door())
            elif which_door == "Blue":
                print(get_blue_door())
            else:
                print(get_door_else())
        elif swim_or_wait == "Swim":
            print(get_swim())
        else:
            print(get_swim_or_wait_else())
    elif left_or_right == "Right":
        print(get_right())
    else:
        print(get_left_or_right_else())


# APP STARTS HERE
if __name__ == "__main__":
    main()
