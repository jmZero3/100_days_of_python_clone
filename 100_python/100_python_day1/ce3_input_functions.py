# def get_name_len():
#     print(len(input("What is your name? ")))


# get_name_len()

def get_name():
    name = input("What is your name? ")
    return name


def get_name_len_without_space(name):
    return len(name) - name.count(" ")


# main is a special function to run the program. so its acceptable to run multiple smaller tasks/functions
def main():
    # ! you can assign a function in a variable.
    name = get_name()
    len_without_space = get_name_len_without_space(name)
    print(len_without_space)


# program starts here
# ! this is called name-main idiom. it is a way to execute code only when the file is being run as a script, but will be skipped if in a module
if __name__ == "__main__":
    main()
