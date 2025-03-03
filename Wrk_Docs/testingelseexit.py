import sys

i = 0
while i < 4:
    if i == 3:
        print(f"You exceeded max num tries {i}, exiting program")
        exit(0)
        # break
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
# dont need import sys provides e==same exigt as break in this instance.
# maybe use if program was going into another function or different loop
