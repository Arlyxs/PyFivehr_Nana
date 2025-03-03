import sys


def dys_convert(num_of_days, unit):
    i = 0
    while i < 4:
        try:
            num_of_days = int(input("Enter a number of days: "))
            if num_of_days > 0:
                # Don't return here, just break the loop
                break
            elif num_of_days == 0:  # check if the number of days is 0
                print("You entered 0, please enter a positive number")
                i += 1
                if i == 3:
                    print(f"You exceeded max num tries {i}, exiting program")
                    exit(0)
            elif num_of_days < 0:
                print(
                    "You entered a negative number of days, please enter a positive number"
                )
                i += 1
                if i == 3:
                    print(f"You exceeded max num tries {i}, exiting program")
                    exit(0)
            else:
                print(f"You failed to enter a viable num.  restart to try again later")
                break
        except ValueError:
            print("You entered an invalid input, please enter a valid number")
            i += 1
            if i == 3:
                print(f"You exceeded max num tries {i}, exiting program")
                exit(0)

    n = 0
    while n < 5:
        try:
            unit = input("Enter the unit, eg. minutes, seconds, hours: ")
            if unit == "hours" or unit == "minutes" or unit == "seconds":
                # Don't return here, just break the loop
                break
            else:
                print("You entered an invalid unit, please enter a valid unit")
                n += 1
                if n == 4:
                    print(f"You exceeded max num tries {i}, exiting program")
                    exit(0)
                continue
        except ValueError:
            print("Unit format is incorrect, please enter a valid unit format")
            n += 1
            if n == 4:
                print(f"You exceeded max num tries {i}, exiting program")
                exit(0)
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

# Remove this line as it's overwriting the unit variable with the entire tuple
# unit = dys_func(num_of_days, unit)


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
