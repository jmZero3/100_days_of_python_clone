def target_number():
    return int(input())


def get_sum_of_even_numbers(target):
    even_sum = 0

    for num in range(0, (target) + 1):
        if num % 2 == 0:
            even_sum += num

    return even_sum


def main():
    target = target_number()
    even_sum = get_sum_of_even_numbers(target)

    print(even_sum)


if __name__ == "__main__":
    main()
