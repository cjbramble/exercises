def get_people_count():
    people_count = int(input("How many people? "))
    return people_count


def get_pizza_count():
    pizzas_count = int(input("How many pizzas do you have? "))
    return pizzas_count


def get_slices_per_pizza_count():
    slices_per_pizza_count = int(input("How many slices do the pizzas have? "))
    return slices_per_pizza_count


def calculate_total_slices(pizzas_count, slices_per_pizza_count):
    total_slices = pizzas_count * slices_per_pizza_count
    return total_slices


def calculate_slices_per_person(total_slices, people_count):
    slices_per_person = total_slices / people_count
    return slices_per_person


def calculate_remaining_slices(total_slices, people_count):
    remaining_slices = total_slices % people_count
    return remaining_slices


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
