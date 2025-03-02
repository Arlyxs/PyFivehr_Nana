# Python basics
# powerful language, many libraries:  web development with Django or Flask, data analysis with pandas, machine learning with scikit-learn, and more.
# Python is an interpreted language, which means that it is not compiled like Java or C++.
# Python is dynamically typed, which means that you don't have to declare the type of a variable when you create one.
# Python is well suited for object-oriented programming.
# Python is a high-level language, which means it abstracts from the computer, making it easier to write code.
# Python is an interpreted language, which means that it is not compiled like Java or C++.
# Python is dynamically typed, which means that you don't have to declare the type of a variable when you create one.
# data collection with web scrapers libraries like BeautifulSoup, Scrapy, and Selenium.
# Python is a popular language for data analysis, with libraries like pandas, NumPy, and matplotlib.
# Python is a popular language for machine learning, with libraries like scikit-learn, TensorFlow, and PyTorch.
# automation with libraries like pyautogui, pywinauto, and pyautogui.

# concatenate strings and numbers in print with format (f)
print("20 days are " + str(28800) + " minutes")
print(f"20 days are {28,800} minutes")
print(f"20 days are {20 * 24 * 60} minutes")

# Variables
# separate multiple words with underline between them
# Variables are case-sensitive

num_of_days = int(input("Enter a number of days: "))
unit = input("Enter the unit, eg. minutes, seconds, hours: ")


hours = num_of_days * 24
minutes = hours * 60
seconds = minutes * 60
calcualtion_to_minutes = hours * 60
calculation_to_seconds = minutes * 60


print(f"{num_of_days} days are {calcualtion_to_minutes} {unit}")
print(f"{num_of_days} days are {calculation_to_seconds} {unit}")

print("++++++++++++++++++++++++")

# functions are blocks of code that are reusable
# functions are defined with the def keyword
# functions can take arguments
# functions can return values
# functions are called with parentheses
# functions can have default arguments
# functions can have keyword arguments


def days_to_units(num_of_days, unit, custom_message):

    if unit == "hours":
        return f"{num_of_days} days are {hours} {unit} {custom_message}"
    elif unit == "minutes":
        return f"{num_of_days} days are {minutes} {unit}  {custom_message}"
    elif unit == "seconds":
        return f"{num_of_days} days are {seconds} {unit} {custom_message}"
    else:
        return "unit not recognized"


dys_units = days_to_units(num_of_days, unit, "Awesome")
print(dys_units)
print(days_to_units(num_of_days, unit, "Great Stuff!"))

print("++++++++++++++++++++++++")
