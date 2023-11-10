import random


def ask_names():
    return input("Give me everybody's names, separated by a comma.\n")


def names_split(names):
    names = names.split(",")
    return names

# ! Once the names have been split you need to be able to call the name by calling its index number
# ! use random.randrange() with 0 as the start and the length of the list as the stop value. You can assign the int as your index number for the list
# ! Once your list is index, whatever value randrange returns will also return the value in that index position.


def get_random_names(names):
    random_names = random.randrange(0, len(names) - 1)
    return names[random_names]


def main():
    names = ask_names()
    names_list = names_split(names)
    random_names = get_random_names(names_list)
    print(f"{random_names} is going to buy the meal today!")


if __name__ == "__main__":
    main()
