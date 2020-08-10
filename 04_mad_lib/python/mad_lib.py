def get_verb():
    return input("Enter a verb: ")


def get_adjective():
    return input("Enter an adjective: ")


def get_noun():
    return input("Enter a noun: ")


def get_adverb():
    return input("Enter an adverb: ")


def print_results(verb, adjective, noun, adverb):
    print(f"Do you {verb} your {adjective} {noun} {adverb}?\nThat\'s hilarious!")


def main():
    print_results(get_verb(), get_adjective(), get_noun(), get_adverb())


if __name__ == "__main__":
    main()
