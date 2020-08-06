def get_person():
    person = input("Who said it? ")
    return person


def get_quote():
    quote = input("What is your quote? ")
    return quote


def print_results(quote, person):
    print(f"{person} says, '{quote}'")


if __name__ == "__main__":
    print_results(get_person(), get_quote())
