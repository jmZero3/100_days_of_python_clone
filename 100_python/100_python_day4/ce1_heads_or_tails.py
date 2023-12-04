import random


def get_randint(x, y):
    return random.randint(x, y)


def main():
    coin = get_randint(0, 1)

    if coin == 1:
        print("Heads")
    else:
        print("Tails")


if __name__ == "__main__":
    main()
