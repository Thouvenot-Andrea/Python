def number(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n


def main():
    for n in range(1, 101):
        print(number(n))


if __name__ == "__main__":
    main()
