def get_pizza_size():
    return input("What size pizza do you want? S, M, L ")


def get_pepperoni():
    return input("Do you want pepperoni? Y or N ")


def get_extra_cheese():
    return input("Do you want extra cheese? Y or N ")


def get_pizza_size_price(ask_pizza_size):
    pizza_size_price = 0
    if ask_pizza_size == "S".lower():
        pizza_size_price += 15
        return pizza_size_price
    elif ask_pizza_size == "M".lower():
        pizza_size_price += 20
        return pizza_size_price
    elif ask_pizza_size == "L".lower():
        pizza_size_price += 25
        return pizza_size_price
    else:
        return print("Invalid Order")


def get_small_pizza(pizza_size_price, ask_pepperoni, ask_extra_cheese):

    if ask_pepperoni == "Y".lower() and ask_extra_cheese == "Y".lower():
        pizza_size_price += 3
        return pizza_size_price
    elif ask_pepperoni == "Y".lower() and ask_extra_cheese == "N".lower():
        pizza_size_price += 2
        return pizza_size_price
    elif ask_pepperoni == "N".lower() and ask_extra_cheese == "Y".lower():
        pizza_size_price += 1
        return pizza_size_price
    else:
        return pizza_size_price


def get_medium_pizza(pizza_size_price, ask_pepperoni, ask_extra_cheese):

    if ask_pepperoni == "Y".lower() and ask_extra_cheese == "Y".lower():
        pizza_size_price += 4
        return pizza_size_price
    elif ask_pepperoni == "Y".lower() and ask_extra_cheese == "N".lower():
        pizza_size_price += 3
        return pizza_size_price
    elif ask_pepperoni == "N".lower() and ask_extra_cheese == "Y".lower():
        pizza_size_price += 1
        return pizza_size_price
    else:
        return pizza_size_price


def get_large_pizza(pizza_size_price, ask_pepperoni, ask_extra_cheese):

    if ask_pepperoni == "Y".lower() and ask_extra_cheese == "Y".lower():
        pizza_size_price += 4
        return pizza_size_price
    elif ask_pepperoni == "Y".lower() and ask_extra_cheese == "N".lower():
        pizza_size_price += 3
        return pizza_size_price
    elif ask_pepperoni == "N".lower() and ask_extra_cheese == "Y".lower():
        pizza_size_price += 1
        return pizza_size_price
    else:
        return pizza_size_price


def get_final_bill(pizza_size_price):
    return print(f"your final bill is ${pizza_size_price}")


def main():
    print("Welcome to Python Pizza Deliveries!")
    ask_pizza_size = get_pizza_size()
    ask_pepperoni = get_pepperoni()
    ask_extra_cheese = get_extra_cheese()
    pizza_size_price = get_pizza_size_price(ask_pizza_size)

# ! you can call the functions and pass arguments within the if else/statement
# ! i find that you cant add any lines of code after if/else statement. It cannot be accessed.
# ! so you can pass all the functions inside the if/else statement and return its result in a return statement

    if ask_pizza_size == "S".lower():
        final_price = get_small_pizza(
            pizza_size_price, ask_pepperoni, ask_extra_cheese)
        return get_final_bill(final_price)
    elif ask_pizza_size == "M".lower():
        final_price = get_medium_pizza(
            pizza_size_price, ask_pepperoni, ask_extra_cheese)
        return get_final_bill(final_price)
    elif ask_pizza_size == "L".lower():
        final_price = get_large_pizza(
            pizza_size_price, ask_pepperoni, ask_extra_cheese)
        return get_final_bill(final_price)
    else:
        return print("Invalid Order")

# APP STARTS HERE


if __name__ == "__main__":
    main()
