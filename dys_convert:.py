import sys


def dys_convert(num_of_days, unit):
    i = 0
    while i < 4:
        if i == 3:
            print(f"You exceeded max num tries {i}, exiting program")
            # exit(0) USE in final program only
            break
        try:
            num_of_days = int(input("Enter a number of days: "))
            if num_of_days > 0:
                break

            elif num_of_days == 0:  # check if the number of days is 0
                print("You entered 0, please enter a positive number")
                i += 1

            elif num_of_days < 0:
                print(
                    "You entered a negative number of days, please enter a positive number"
                )
                i += 1

            else:
                print("You entered an invalid unit, please enter a valid unit")
                i += 1

        except ValueError:
            print("exception error: invalid input type. please enter a valid number")
            i += 1

    n = 0
    while n < 5:
        if n == 4:
            print(f"You exceeded max num tries {n}, exiting program")
            exit(0)
            # break USE for testing only goes on to calc
            # with invalid input type. function = unit not recognized.
        try:
            unit = input("Enter the unit, eg. minutes, seconds, hours: ")
            if unit == "hours" or unit == "minutes" or unit == "seconds":
                break
            else:
                print("You entered an invalid unit, please enter a valid unit")
                n += 1
        except ValueError:
            print(
                "exception error: invalid input type. please enter a valid unit format"
            )
            n += 1

    # Calculate the values after both inputs are collected
    calc_to_hours = num_of_days * 24
    calc_to_minutes = calc_to_hours * 60
    calc_to_seconds = calc_to_minutes * 60

    return num_of_days, unit, calc_to_hours, calc_to_minutes, calc_to_seconds


num_of_days = 0
unit = ""
num_of_days, unit, calc_to_hours, calc_to_minutes, calc_to_seconds = dys_convert(
    num_of_days, unit
)


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
