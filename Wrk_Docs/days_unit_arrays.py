# multiple line comments""" e.g.
"""" use content e"""


# verify user input and send to dys_to_units() for calculation
def validate_and_execute():
    try:
        # :- ensures that user enters a positive integer
        # previous code: user_input_number = int(num_of_days)
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")
        else:
            print("you entered a negarive number, no conversion for you")

    except ValueError:
        print("your input is not a valid number,  Don't ruin my program")


# :- calculate days to hours static resource inputs
calculation_to_units = 24
name_of_unit = "hours"


# :- calculate dys to units and return result
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


# gets user data input (lists and converts to set) sends to validate and execute()
user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, enter a number of days as a comma separated list and i will convert it to hours\n"
    )
    # previous code: print(user_input.split(","))
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    # previous code:for num_of_days_element in user_input.split(","):
    # :- split takes individual entries and creats list.  "," takes comm separated list.  default is spaces converted to list
    # previous code: for num_of_days_element in user_input.split(","):
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
