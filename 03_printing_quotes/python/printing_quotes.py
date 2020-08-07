def get_person():
    person = input("Who said it? ")
    return person


def get_quote():
    quote = input("What is your quote? ")
    return quote


def print_results(person, quote):
    # concatenation is a constraint of the exercise
    print(person + " says, " + "\'" + quote + "\'")


def main():
    person = get_person()
    quote = get_quote()
    print_results(person, quote)


if __name__ == "__main__":
    main()
