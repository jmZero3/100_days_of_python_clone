def ask_student_scores():
    return input().split()


def student_scores_list(student_scores):

    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])

    return student_scores


def get_high_student_score(student_scores):

    student_high_score = 0
    for score in student_scores:
        if score > student_high_score:
            student_high_score = score

    return student_high_score


def main():
    ask_scores = ask_student_scores()
    student_scores = student_scores_list(ask_scores)
    student_high_score = get_high_student_score(student_scores)

    print(f"Ths highest score in the class is {student_high_score}")


# APP STARTS HERE
if __name__ == "__main__":
    main()
