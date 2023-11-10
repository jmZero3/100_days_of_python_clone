# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# TODO define functions. These 2 functions convert str inputs to int values or "subscript" str


def find_first_digit():
    get_first_digit = int(two_digit_number[0])
    return get_first_digit


def find_second_digit():
    get_second_digit = int(two_digit_number[1])
    return get_second_digit

# TODO define a function that adds the return value of the 2 function. Note that you cannot add function to function.
# TODO to be able to add the values, you must initialize 2 variables that call the functions that will return the value. You can then add the two together
# TODO to be able to do mathematical operationsbetween 2 variable, initialize variables that calls a function
# TODO return print statement


def combine_result():
    first_digit = find_first_digit()
    second_digit = find_second_digit()
    return print(first_digit + second_digit)

# APP STARTS HERE


combine_result()
