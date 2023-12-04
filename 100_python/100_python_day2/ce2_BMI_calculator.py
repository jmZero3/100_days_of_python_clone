
# TODO define functions to get height and weight
# TODO in this function take in the input and subscript it to float values and return its value
def get_height():
    height = input("enter your height in m: ")
    convert_height = float(height)
    return convert_height


def get_weight():
    weight = input("enter your weight in kg: ")
    convert_weight = float(weight)
    return convert_weight

# TODO define function that calls get_height() and get_weight() in a variable. initialize another variable calculating bmi and convert value into int
# TODO return print statement


def get_bmi():
    height = get_height()
    weight = get_weight()
    bmi_as_int = int(weight / height ** 2)
    return print(bmi_as_int)


# APP STARTS HERE
get_bmi()
