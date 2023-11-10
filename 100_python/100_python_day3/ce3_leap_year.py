def get_year_to_check():
    ask_year = int(input("Which year do you want to check? "))
    return ask_year

# ! you can use multiple return statements in a function that contains if/else statements
# ! this is a single if/else statement with multiple conditions
# ! defining this function, you can just return string without using the print() function


def get_leap_or_not_leap_year(ask_year):
    if ask_year % 4 == 0:
        if ask_year % 100 == 0:
            if ask_year % 400 == 0:
                return "Leap year."
            else:
                return "Not leap year."
        else:
            return "Leap year."
    return "Not leap year."


def main():
    ask_year = get_year_to_check()
    is_leap_year = get_leap_or_not_leap_year(ask_year)
    print(is_leap_year)


if __name__ == "__main__":
    main()
