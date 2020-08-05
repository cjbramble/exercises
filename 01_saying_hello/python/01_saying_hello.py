def get_name():
    name = input("What is your name? ")
    return name


def print_name(name):
    print(f"Hello {name}, nice to meet you!")


if __name__ == "__main__":
    print_name(get_name())
