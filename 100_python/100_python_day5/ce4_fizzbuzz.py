

def main():
    target = 100

    for number in range(0, (target) + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('fizzbuzz')
        elif number % 3 == 0:
            print('fizz')
        elif number % 5 == 0:
            print('buzz')
        else:
            print(number)


if __name__ == "__main__":
    main()
