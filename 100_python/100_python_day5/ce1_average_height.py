def get_heights():
    return input().split()


def get_height_list(student_heights):
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    return student_heights


def get_height_sum(student_heights):

    total_height = 0

    for height in student_heights:
        total_height += height

    return total_height


def get_number_of_students(student_heights):

    number_of_students = 0

    for number in student_heights:
        number_of_students += 1

    return number_of_students


def get_height_average(student_heights, total_height):

    average_height = 0

    for student in student_heights:
        average_height = total_height / len(student_heights)

    return round(average_height)


def main():

    student_heights = get_heights()

    list_of_student_heights = get_height_list(student_heights)

    total_height = get_height_sum(list_of_student_heights)

    number_of_students = get_number_of_students(student_heights)

    average_height = get_height_average(
        student_heights, total_height)

    print(
        f"\ntotal height = {total_height}\nnumber of students = {number_of_students}\naverage height = {average_height}")


if __name__ == "__main__":
    main()
