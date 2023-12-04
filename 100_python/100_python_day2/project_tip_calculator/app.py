# Tip calculator app by Julius Morales
# This app takes the total bill and tip and divides it up within a group of people to pay

# TODO Create function for bill


def ask_bill():
    bill_total = float(input(" What was the total bill? $"))
    return bill_total


def get_bill(bill_total):
    return bill_total


# TODO Create function for tip percentage


def ask_tip_percent():
    tip_total = int(input("What percentage tip would you like to give? "))
    return tip_total


def get_tip_percentage(tip_total):
    return 1.0 + (tip_total / 100)

# TODO Create function for how many people to split the bill


def ask_split_total():
    people_to_split = int(input("How many people to split the bill? "))
    return people_to_split


def get_split_total(people_to_split):
    return people_to_split

# TODO Create function that calculates how much a person should pay


def get_person_total_pay(bill_total, people_to_split, tip_total):
    return (bill_total / people_to_split) * tip_total

# TODO Create function main()


def main():
    print("Welcome to the tip calculator!")
    ask_for_bill = ask_bill()
    bill_total = get_bill(ask_for_bill)
    ask_for_tip = ask_tip_percent()
    tip_total = get_tip_percentage(ask_for_tip)
    ask_for_split = ask_split_total()
    people_to_split = get_split_total(ask_for_split)
    bill_per_person = get_person_total_pay(
        bill_total, people_to_split, tip_total)
    return print(f"Each person should pay: ${bill_per_person:.2f}")

# APP STARTS HERE


if __name__ == "__main__":
    main()
