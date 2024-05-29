from FizzBuzz.fizzbuzz import number


def test_three():
    actual = number(3)
    expected = "fizz"
    assert actual == expected


def test_five():
    actual = number(5)
    expected = "buzz"
    assert actual == expected


def test_five_three():
    actual = number(15)
    expected = "fizzbuzz"
    assert actual == expected
