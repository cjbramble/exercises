
def get_input():
    input_string = None

    while not input_string:
        return input("What is your input string? ")


def print_results(input_string):
    print(input_string, "has", len(input_string), "characters.")


def main():
    input_string = get_input()
    print_results(input_string)


if __name__ == "__main__":
    main()
