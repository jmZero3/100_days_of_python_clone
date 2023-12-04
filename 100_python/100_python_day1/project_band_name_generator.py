# 1. Create a greeting for your program.
# print("Welcome to the Band Name Generator!")
# 2. Ask the user for the city that they grew up in.
# city = input("What city did you grow up in?\n")
# 3. Ask the user for the name of a pet.
# pet = input("what is the name of your pet?\n")
# 4. Combine the name of their city and pet and show them their band name.
# band_name = print(f"your band name could be {city} {pet}!")
# 5. Make sure the input cursor shows on a new line:


def get_city():
    city = input("What city did you grow up in?\n")
    return city


def get_pet():
    pet = input("What is the name of your pet?\n")
    return pet


def main():
    print("Welcome to the Band Name Generator!")
    city = get_city()
    pet = get_pet()
    print(f"your band name could be {city} {pet}!")


# program starts here

if __name__ == "__main__":
    main()
