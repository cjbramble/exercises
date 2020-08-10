def get_people_count():
    return int(input("How many people? "))


def get_pizza_count():
    return int(input("How many pizzas do you have? "))


def get_slices_per_pizza_count():
    return int(input("How many slices do the pizzas have? "))


def calculate_total_slices(pizzas_count, slices_per_pizza_count):
    return pizzas_count * slices_per_pizza_count


def calculate_slices_per_person(total_slices, people_count):
    return total_slices / people_count


def calculate_remaining_slices(total_slices, people_count):
    return total_slices % people_count


def main():
    people_count = get_people_count()
    pizzas_count = get_pizza_count()
    slices_per_pizza_count = get_slices_per_pizza_count()
    total_slices = calculate_total_slices(pizzas_count, slices_per_pizza_count)
    print(f"{people_count} people with {pizzas_count} pizzas.")
    slices_per_person = calculate_slices_per_person(total_slices, people_count)
    print(f"Each person gets {slices_per_person} pieces of pizza.")
    remaining_slices = calculate_remaining_slices(total_slices, people_count)
    print(f"There are {remaining_slices} slices leftover.")


if __name__ == "__main__":
    main()
