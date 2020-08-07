def get_name():
    name = input("What is your name? ")
    return name


def print_name(name):
    print(f"Hello {name}, nice to meet you!")


def main():
    name = get_name()
    print_name(name)


if __name__ == "__main__":
    main()
