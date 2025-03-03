def days_to_units(num_of_days, unit, custom_message):
    if num_of_days > 0:
        num_of_days
    elif num_of_days == 0:
        return "You entered 0, please enter a positive number"
    else:
        return "You entered a negative number of days, please enter a positive number"
    if unit == "hours" or unit == "minutes" or unit == "seconds":
        unit
    else:
        return "You entered an invalid unit, please enter a valid unit"

    num_of_days = int(input("Enter a number of days: "))
    unit = input("Enter the unit, eg. minutes, seconds, hours: ")

    calc_to_hours = num_of_days * 24
    calc_to_minutes = calc_to_hours * 60
    calc_to_seconds = calc_to_minutes * 60

    if unit == "hours":
        return f"{num_of_days} days are {calc_to_hours} {unit} {custom_message}"
    elif unit == "minutes":
        return f"{num_of_days} days are {calc_to_minutes} {unit}  {custom_message}"
    elif unit == "seconds":
        return f"{num_of_days} days are {calc_to_seconds} {unit} {custom_message}"
    else:
        return "unit not recognized"


# need to put return here and not in body of function
# need to return all variables for use in dys_units function


dys_units = days_to_units(num_of_days, unit, "Awesome\n")
print(dys_units)
print(days_to_units(num_of_days, unit, "Great Stuff!"))
