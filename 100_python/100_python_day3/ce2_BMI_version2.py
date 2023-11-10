def get_height():
    height = input("enter your height in m: ")
    convert_height = float(height)
    return convert_height


def get_weight():
    weight = input("enter your weight in kg: ")
    convert_weight = float(weight)
    return convert_weight


def get_bmi(weight, height):
    bmi_round = round(weight / height ** 2)
    return bmi_round

# ! you can return the f-string statement without the need of assigning it to a variable and you also dont need the print() function
# ! print function just ouputs value, but it does not return a value


def bmi_spectrum(bmi_round):
    if bmi_round < 18.5:
        return f"Your BMI is {bmi_round}, you are underweight."
    elif bmi_round < 25:
        return f"Your BMI is {bmi_round}, you are normal weight."
    elif bmi_round < 30:
        return f"Your BMI is {bmi_round}, you are slightly overweight."
    elif bmi_round < 35:
        return f"Your BMI is {bmi_round}, you are obese."
    else:
        return f"Your BMI is {bmi_round}, you are clinically obese."


def main():
    height = get_height()
    weight = get_weight()
    bmi_round = get_bmi(weight, height)
    bmi_range = bmi_spectrum(bmi_round)
    print(bmi_range)


# APP STARTS HERE
if __name__ == "__main__":
    main()
