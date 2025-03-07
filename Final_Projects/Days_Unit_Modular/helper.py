# verify user input and send to dys_to_units for calculation
def validate_and_execute(days_and_unit_dictionary):
    try:
        # :- ensures that user enters a positive integer
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(
                user_input_number, days_and_unit_dictionary["unit"]
            )
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")
        else:
            print("you entered a negarive number, no conversion for you")

    except ValueError:
        print("your input is not a valid number,  Don't ruin my program")


user_input_message = "Hey user, enter a number of days and conversion unit!\n"


# :- calculate dys to units and return result
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"
