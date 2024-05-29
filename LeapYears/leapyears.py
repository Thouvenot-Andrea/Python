# divisible par 400 bissextile
# divisible par 100 mais pas par 400 non bissextile
# divisible par 4 mais pas par 100  bissextile
# divisible pas par 4 non bissextile
def is_leap_year(year):
    if year % 400 == 0:
        return "Année bissextile"
    elif year % 100 == 0:
        return "Année non bissextile"
    elif year % 4 == 0:
        return "Année bissextile"
    else:
        return "Année non bissextile"


def main():
    year = int(input())
    print(is_leap_year(year))


if __name__ == '__main__':
    main()
