from app import get_bill, get_split_total, get_tip_percent


def test_bill():
    bill = get_bill()
    assert bill == get_bill()
