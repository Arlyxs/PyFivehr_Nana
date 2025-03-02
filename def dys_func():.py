def dys_func():
    i = 0
    while i < 4:
        try:
            num_of_days = int(input("Enter a number of days: "))
            if num_of_days > 0:
                num_of_days
                i += 1
                break
            elif num_of_days == 0:  # check if the number of days is 0
                print("You entered 0, please enter a positive number")
                i += 1
                if i == 3:
                    print(f"You exceeded max num tries {i}, please try again later")
                    break
            elif num_of_days < 0:
                print(
                    "You entered a negative number of days, please enter a positive number"
                )
                i += 1
                if i == 3:
                    print(f"You exceeded max num tries {i}, please try again later")
                    break
            else:
                print(f"You failed to enter a viable num.  restart ot try again later")
                break
        except ValueError:
            print("You entered an invalid input, please enter a valid number")
            i += 1
            if i == 3:
                print(f"You exceeded max num tries {i}, please try again later")
                break
    
    n = 0
    while n in range(5):
        try:
            unit = input("Enter the unit, eg. minutes, seconds, hours: ")
            if unit == "hours" or unit == "minutes" or unit == "seconds":
                unit
                n += 1
                break
            else:
                print("You entered an invalid unit, please enter a valid unit")
                n += 1
                if n == 4:
                    print(f"You exceeded max num tries {n}, please try again later")
                    break
        except ValueError:
            print("Unit format is incorrect, please enter a valid number")
            n += 1
            if n == 4:
                print(f"You exceeded max num tries {i}, please try again later")
                break

    if unit == "hours":
            return f"{num_of_days} days are {calc_to_hours} {unit} {custom_message}"
        elif unit == "minutes":
            return f"{num_of_days} days are {calc_to_minutes} {unit}  {custom_message}"
        elif unit == "seconds":
            return f"{num_of_days} days are {calc_to_seconds} {unit} {custom_message}"
        else:
            return "unit not recognized"

dys_func()
