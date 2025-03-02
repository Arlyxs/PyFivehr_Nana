# converts days to hour/mins/secs

# global variables

while True:
    try:
        num_of_days = int(input("Enter a number of days: "))
        if num_of_days > 0:
            num_of_days
            break
        elif num_of_days == 0:  # check if the number of days is 0
            print("You entered 0, please enter a positive number")
        else:
            print(
                "You entered a negative number of days, please enter a positive number"
            )
    except ValueError:
        print
        # ("You entered an invalid input, please enter a valid number")
        continue
while True:
    try:
        unit = input("Enter the unit, eg. minutes, seconds, hours: ")
        if unit == "hours" or unit == "minutes" or unit == "seconds":
            unit
            break
        else:
            print("You entered an invalid unit, please enter a valid unit")
    except ValueError:
        print
        ("You entered an invalid input, please enter a valid unit")

calc_to_hours = num_of_days * 24
calc_to_minutes = calc_to_hours * 60
calc_to_seconds = calc_to_minutes * 60


def days_to_units(num_of_days, unit, custom_message):

    if unit == "hours":
        return f"{num_of_days} days are {calc_to_hours} {unit} {custom_message}"
    elif unit == "minutes":
        return f"{num_of_days} days are {calc_to_minutes} {unit}  {custom_message}"
    elif unit == "seconds":
        return f"{num_of_days} days are {calc_to_seconds} {unit} {custom_message}"
    else:
        return "unit not recognized"


dys_units = days_to_units(num_of_days, unit, "Awesome\n")
print(dys_units)
print(days_to_units(num_of_days, unit, "Great Stuff!"))
