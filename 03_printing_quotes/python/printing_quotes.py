def get_person():
    return input("Who said it? ")


def get_quote():
    return input("What is your quote? ")


def print_results(person, quote):
    # concatenation is a constraint of the exercise
    print(person + " says, " + "\'" + quote + "\'")


def main():
    person = get_person()
    quote = get_quote()
    print_results(person, quote)


if __name__ == "__main__":
    main()
