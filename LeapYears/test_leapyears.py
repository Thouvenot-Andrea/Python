from LeapYears.leapyears import is_leap_year


def test_leap_years_divisible():
    actual = is_leap_year(2000)
    expected = "Année bissextile"
    assert actual == expected


def test_leap_years_not_divisible():
    actual = is_leap_year(2001)
    expected = "Année non bissextile"
    assert actual == expected


def test_leap_years_divisible_by_100_but_not_400():
    actual = is_leap_year(2100)
    expected = "Année non bissextile"
    assert actual == expected


def test_leap_years_divisible_by_4_but_not_100():
    actual = is_leap_year(2024)
    expected = "Année bissextile"
    assert actual == expected
