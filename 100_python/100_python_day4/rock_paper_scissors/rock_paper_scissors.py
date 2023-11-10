import random

# ask user to choose rock, paper, scissor represented by an integer


def ask_user_choice():
    return int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# set up computer random choice


def get_random_choice(start, stop):
    return random.randint(start, stop)


def user_choice_print(user, rock, paper, scissors):
    if user == 0:
        return rock
    elif user == 1:
        return paper
    elif user == 2:
        return scissors
    else:
        return "You typed an invalid number"


def computer_choice_print(computer, rock, paper, scissors):
    if computer == 0:
        return rock
    elif computer == 1:
        return paper
    elif computer == 2:
        return scissors


# set up logic for win lose or draw conditions

def win_lose_draw(user, computer, rock, paper, scissors):
    if user == rock and computer == scissors:
        return "You win!"
    elif user == rock and computer == paper:
        return "You lose"
    elif user == paper and computer == rock:
        return "You win!"
    elif user == paper and computer == scissors:
        return "You lose"
    elif user == scissors and computer == paper:
        return "You win!"
    elif user == scissors and computer == rock:
        return "You lose"
    elif user == computer:  # ! easier code condition. if user and computer have the same choice then draw rather than type out all the possible conditions
        return "Its a draw"
    else:
        "You typed invalid option: you lose"


#  run main script

def main():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
             _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
          __________)
           (____)
    ---.__(___)
    '''

    user = ask_user_choice()
    computer = get_random_choice(0, 2)

    user_choice = user_choice_print(user, rock, paper, scissors)
    computer_choice = computer_choice_print(computer, rock, paper, scissors)
    result = win_lose_draw(user_choice, computer_choice, rock, paper, scissors)

    print(f"{user_choice}\nComputer chose:{computer_choice}\n{result}")


# APP STARTS HERE
if __name__ == "__main__":
    main()
