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
print("20 days are " + str(28800) + " minutes \n")
# \n will print to a new line before or after text where placed

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


dys_units = days_to_units(num_of_days, unit, "Awesome\n")
print(dys_units)
print(days_to_units(num_of_days, unit, "Great Stuff!"))

print("++++++++++++++++++++++++")

# lists
# lists are used to store multiple items in a single variable
# Python has foyr built_in data sets: Lists, tuple, Set and Dictionary

# Lists square brackers []
myList = ["apple", "bananas", "cherry"]
print("\n" + myList[0] + "\n")
print(myList)
# "\n" new line before asd + "\n" newline after

# lists have  a defined order that wil not change.  NEW items placed
# at the end of the list.  can change items in the list, add,remove
# unlike Sets list have have duplicate items
# can have any data type

this_list = ["abc", 34, True, 40, False, "male"]
print(type(this_list))

# list constructor
thisList = list(("apple", "band", 50))
print(thisList)

# thisList. (append, remove, reverse, pop etc.)

# PYTHON COLLECTIOS - ARRAYS

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning,
# and, it could mean an increase in efficiency or security.

# MODULES
# a module contains functions or variables that you can use in another python file.
# you can reference one module from another - can structure program using modules
# called making the program modular

# import <module name> : imports the modules functions and variable to the target need <module name>.function or variable
# import * :  imports everything (all)from the module to the target no <name>.funciton or variable required
# items in module referred to as definiiton.  so import definitions from another file to a target
# can create an alias for modules when doing an import reference import <mod_name> as <new name
# omport <module> <definition> so if only definition used then from <module name> import <definition>

# THIRD PARTY MODULES
# online search for *** pypi.org *** Python package index : listing of packages and modules appears.
# a module is a python file; a package is a collection of modules
# package has __init__ file to distinguish it from a normal python
# can publish your own modules or packages

# WEB DEVELOPMENT numpy, Django
# packages can be installed in python using *** pip*** package manager python install/remove package
# alibrary is a collection of packages for python

# import openpyxl for ms excel fils
# import pyexcel_ods for open document file
# OBJECT ORIENTED PROGRAMMING
# CLASSES
# class is an object constructor
# all classes have __init__() function
# __init--() is exectued automatically, whenever we creat the
# objects from this class
# self parameter is a reference to the current instance of the class
# is used to access variables that belong to the class

# functions that belong to an object are called methods

# Almost everything in Python is an object
# str(), int(), ... are the constructor function built into Python

# SEARCH for site API request and send data
# git lab api documentation
