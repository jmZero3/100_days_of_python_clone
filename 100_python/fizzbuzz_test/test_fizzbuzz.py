from fizzbuzz import fizz

# TODO run pytest on the terminal
# TODO when writing a test. first create a function that calls on the function you want to test for
# TODO set up a variable to call the function you are testing for
# TODO use keyword assert followed by the variable == desired outcome/value. This ensures that your test is properly executing
# TODO write function logic (if applies)
# TODO call function and give a value to test
# TODO with pytest assert, it only checks if code is returning expected value. Actual value vs. expected value


def test_fizz():
    get_fizz = fizz(3)
    assert get_fizz == "fizz"
