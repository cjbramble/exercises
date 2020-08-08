def get_noun():
    noun = input("Enter a noun: ")
    return noun


def get_verb():
    verb = input("Enter a verb: ")
    return verb


def get_adjective():
    adjective = input("Enter an adjective: ")
    return adjective


def get_adverb():
    adverb = input("Enter an adverb: ")
    return adverb


def print_results(verb, adjective, noun, adverb):
    print(f"Do you {verb} your {adjective} {noun} {adverb}?\nThat\'s hilarious!")


def main():
    print_results(get_noun(), get_verb(), get_adverb(), get_adjective())


if __name__ == "__main__":
    main()
