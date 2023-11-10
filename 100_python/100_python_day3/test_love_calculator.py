from ce5_love_calculator import get_total_true_love_score, get_interpretation


# def test_get_total_true_love_score():
#     total_score = get_total_true_love_score(2, 3)
#     assert total_score == 9


def test_interpretation():
    interpret = get_interpretation(13)
    assert interpret == f"Your score is 13."
