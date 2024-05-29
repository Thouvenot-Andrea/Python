import calc


def test_add_one():
    result = calc.add_one(2)
    assert result == 4


def test_add_two():
    result = calc.add_two(5)
    assert result == 7
