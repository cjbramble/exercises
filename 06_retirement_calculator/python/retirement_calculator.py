import datetime


def get_current_age():
    current_age = int(input("What is your current age? "))
    return current_age


def get_age_to_retire():
    age_to_retire = int(input("At what age would you like to retire? "))
    return age_to_retire


def calculate_years_to_retire(age_to_retire, current_age):
    years_to_retire = age_to_retire - current_age
    return years_to_retire


def get_current_year():
    now = datetime.datetime.now()
    current_year = now.year
    return current_year


def print_years_to_retire(years_to_retire):
    print(f"You have {years_to_retire} years to retire.")


def print_year_of_retirement(current_year, years_to_retire):
    print(f"It's {current_year}, so you can retire in {current_year + years_to_retire}.")


def main():
    age_now = get_current_age()
    age_when = get_age_to_retire()
    year_now = get_current_year()
    years_mathed = calculate_years_to_retire(age_when, age_now)
    print_years_to_retire(years_mathed)
    print_year_of_retirement(year_now, years_mathed)


if __name__ == "__main__":
    main()
