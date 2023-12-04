def get_number():
    number = int(input("Which number do you want to check? "))
    return number


def get_odd_or_even(number):
    if number % 2 == 0:
        return print("This is an even number.")
    else:
        return print("This is an odd number.")


def main():
    ask_for_number = get_number()
    check_number = get_odd_or_even(ask_for_number)
    return check_number


if __name__ == "__main__":
    main()
