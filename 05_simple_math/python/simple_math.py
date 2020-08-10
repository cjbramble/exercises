def get_first_number():
    return int(input("What is the first number? "))


def get_second_number():
    return int(input("What is the second number? "))


def print_results(first_number, second_number):
    fmt_str = "{:d} {} {:d} = {}"

    print(fmt_str.format(first_number, "+", second_number, first_number + second_number))
    print(fmt_str.format(first_number, "-", second_number, first_number - second_number))
    print(fmt_str.format(first_number, "*", second_number, first_number * second_number))
    print(fmt_str.format(first_number, "/", second_number, first_number / second_number))


def main():
    first_int = get_first_number()
    second_int = get_second_number()
    print_results(first_int, second_int)


if __name__ == "__main__":
    main()
