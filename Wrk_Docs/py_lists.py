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
