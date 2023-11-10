
# TODO define 2 functions that takes in current age in years and how long someone wants to live.

def goal_age_expectency():
    # expected_age = int(input("How old do you want to live? "))  -- in case you want to pick a different age
    expected_age = 90
    return expected_age


def get_current_age():
    current_age = int(input("What is your current age? "))
    return current_age

# TODO define functions that convert current age into days, months and weeks.
# TODO each functions return the value of (expected_age - get_age) * days(365),weeks(52),months(12)
# TODO NOTE creating a code block with  calculations BEFORE the return statements caused bugs.
# TODO DO NOT call any functions inside the function if you only intend for a function to only be called once. EX get_current_age was called 3 times unintendedly
# TODO so writing out the logic in the return statement allows it to be defined
# TODO NOTE you can pass in parameter arguments and use it within the return statement.
# TODO NOTE the naming conventions passed into the conversion functions is the same variable names returned in the functions you need to call later and pass in the conversion functions


def get_days(expected_age, get_age):
    return (expected_age - get_age) * 365


def get_months(expected_age, get_age):
    return (expected_age - get_age) * 12


def get_weeks(expected_age, get_age):
    return (expected_age - get_age) * 52

# TODO define main functions that calls goal_age_expectency(), get_current_age() and passes it in the 3 conversion functions. return an f-string print statement


def main():
    expected_age = goal_age_expectency()
    current_years = get_current_age()
    years_in_days = get_days(expected_age, current_years)
    years_in_months = get_months(expected_age, current_years)
    years_in_weeks = get_weeks(expected_age, current_years)
    return print(f"You have {years_in_days} days, {years_in_weeks} weeks, and {years_in_months} months left.")


# APP STARTS HERE
if __name__ == "__main__":
    main()
