from helper import validate_and_execute, user_input_message

# get user input and send for validation and execution
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    if user_input == "exit":
        break

    try:
        days_and_unit = user_input.split(":")
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        validate_and_execute(days_and_unit_dictionary)
    except IndexError:
        print("Please enter your input in the format: number:unit (e.g., 5:hours)")
