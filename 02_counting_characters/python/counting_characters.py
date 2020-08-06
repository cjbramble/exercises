
def get_input():
    input_string = None

    while not input_string:
        input_string = input("What is your input string? ")
    return input_string


def print_results(input_string):
    print(input_string, "has", len(input_string), "characters.")


if __name__ == "__main__":
    print_results(get_input())
