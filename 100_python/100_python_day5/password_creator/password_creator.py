import random


def get_nr_letters():
    return int(input("How many letters would you like in your password?\n"))


def get_nr_symbols():
    return int(input("How many symbols would you like?\n"))


def get_nr_numbers():
    return int(input("How many numbers would you like\n"))


def get_random_letters_list(ask_letters, letters):
    letters_list = []

    for num in range(0, (ask_letters)):
        letters_list.append(random.choice(letters))
    return letters_list


def get_random_symbols_list(ask_symbols, symbols):
    symbols_list = []

    for num in range(0, (ask_symbols)):
        symbols_list.append(random.choice(symbols))
    return symbols_list


def get_random_numbers_list(ask_numbers, numbers):
    numbers_list = []

    for num in range(0, (ask_numbers)):
        numbers_list.append(random.choice(numbers))
    return numbers_list


def compile_list(letters_list, symbols_list, numbers_list):
    password_list = letters_list + symbols_list + numbers_list
    return password_list


def get_scrambled_password(password):
    random.shuffle(password)
    return password


def main():

    print("Welcome to the PyPassword Generator!")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ask_letters = get_nr_letters()
    ask_symbols = get_nr_symbols()
    ask_numbers = get_nr_numbers()

    letters_list = get_random_letters_list(ask_letters, letters)
    symbols_list = get_random_symbols_list(ask_symbols, symbols)
    numbers_list = get_random_numbers_list(ask_numbers, numbers)

    combined_password = compile_list(letters_list, symbols_list, numbers_list)

    shuffled_password = get_scrambled_password(combined_password)

    password = ''.join(shuffled_password)

    print(f"your password is: {password}")

# APP STARTS HERE


if __name__ == "__main__":
    main()
