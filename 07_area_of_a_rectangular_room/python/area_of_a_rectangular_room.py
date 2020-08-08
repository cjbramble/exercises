def get_length():
    length = int(input("What is the length of the room in feet? "))
    return length


def get_width():
    width = int(input("What is the width of the room in feet? "))
    return width


def calculate_area_in_feet(width, length):
    area_in_feet = width * length
    return area_in_feet


def calculate_area_in_meters(area_in_feet):
    area_in_meters = area_in_feet * 0.09290304
    return area_in_meters


def print_area_in_feet(length, width):
    print(f"You entered dimensions of {length} feet by {width} feet.")


def print_area_in_meters(area_in_feet, area_in_meters):
    print(f"The area is\n{area_in_feet} square feet\n{area_in_meters} square meters")


def main():
    lengthed = get_length()
    widthed = get_width()
    feet_area = calculate_area_in_feet(widthed, lengthed)
    meters_area = calculate_area_in_meters(feet_area)
    print_area_in_feet(lengthed, widthed)
    print_area_in_meters(feet_area, meters_area)


if __name__ == "__main__":
    main()
