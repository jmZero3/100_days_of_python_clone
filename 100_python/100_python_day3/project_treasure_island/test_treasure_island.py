from treasure_island import ask_left_or_right, get_left_or_right


def ask_left_or_right_test():
    left_or_right = get_left_or_right("left")
    assert left_or_right == True
