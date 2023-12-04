def get_first_name():
    first_name = input("What is your name?\n")
    return first_name.lower()


def get_second_name():
    second_name = input("What is their name?\n")
    return second_name.lower()


def get_true_count(first_name, second_name):
    first_name = first_name.lower()
    second_name = second_name.lower()
    true_score_t = first_name.count("t") + second_name.count("t")
    true_score_r = first_name.count("r") + second_name.count("r")
    true_score_u = first_name.count("u") + second_name.count("u")
    true_score_e = first_name.count("e") + second_name.count("e")
    total_true_score = true_score_t + true_score_r + true_score_u + true_score_e
    return total_true_score


def get_love_count(first_name, second_name):
    first_name = first_name.lower()
    second_name = second_name.lower()
    love_score_l = first_name.count("l") + second_name.count("l")
    love_score_o = first_name.count("o") + second_name.count("o")
    love_score_v = first_name.count("v") + second_name.count("v")
    love_score_e = first_name.count("e") + second_name.count("e")
    total_love_score = love_score_l + love_score_o + love_score_v + love_score_e
    return total_love_score


# ! 2 ways to do this
# ! commented out code shows a variable that was type cast to string to concatonate total_true_score & total_love_score and type casted back into an int.
'''def get_total_true_love_score(total_true_score, total_love_score):
    true_love_score = int(str(total_true_score) + str(total_love_score))
    return true_love_score'''

# ! this function keeps all data type as integers and executes a mathematical expression to return true_love_score as an int


def get_total_true_love_score(total_true_score, total_love_score):
    true_love_score = total_true_score * 10 + total_love_score
    return true_love_score


# ! so the print function does not return a value so you dont need to include it in the get_interpretation function
def get_interpretation(true_love_score):
    if true_love_score < 10 or true_love_score > 90:
        return f"Your score is {true_love_score}, you go together like coke and mentos."
    elif true_love_score >= 40 and true_love_score <= 50:
        return f"Your score is {true_love_score}, you are alright together."
    else:
        return f"Your score is {true_love_score}."


# ! to show the output when calling get_interpretation you can do it 2 ways

def main():
    print("Welcome to the Love Calculator!")
    first_name = get_first_name()
    second_name = get_second_name()
    total_true_score = get_true_count(first_name, second_name)
    total_love_score = get_love_count(first_name, second_name)
    true_love_score = get_total_true_love_score(
        total_true_score, total_love_score)
    # ! If you only need to output the return value you dont have to store get_interpration() function in a variable. you can do it like this
    # ! print(get_interpretation(true_love_score))
    # ! if you need to call get_interpretation() function multiple times, just store it in a variable to call again
    compatibility = get_interpretation(true_love_score)
    print(compatibility)

# app starts here


if __name__ == "__main__":
    main()
