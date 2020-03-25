# Creates a variable called formatter with a value of 4 curly braces
formatter = "{} {} {} {}"

# Here the formatter variable (the value of which is the string "{} {} {} {}") calls the string formatting method "{}.format". The previous string value of "{} {} {} {}" will be replaced by the integers "1, 2, 3, 4," which will be printed onto the screen
print(formatter.format(1, 2, 3, 4))

# Here the formatter variable (the value of which are the 4 integers "1, 2, 3, 4") calls/uses the string method .format. The previous value of "1, 2, 3, 4" will now be replaced by "one", "two", "three", "four," which will be printed onto the screen
print(formatter.format("one", "two", "three", "four"))

# Here the formatter variable's value will be changed to "True, False, False True," which will then be printed onto the screen
print(formatter.format(True, False, False, True))

# Here the formatter variable's original value of four curly braces is being called. "{} {} {} {}" Since it is being called 4 times, 16 curly braces will be printed (4 sets of curly braces)
print(formatter.format(formatter, formatter, formatter, formatter))

# Here the value of the formatter variable has been changed to the string below. This new value will be printed to the screen.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# Tips for using the .foramt method: When you are using a variable don't use the curly braces after it.
# This is wrong -> formatter{}.format("{}" "{}" "{}" "{}")

# Here the value of hte formatter variable has been changed to "-" "-" "+" "+". This new value will be printed onto the screen.
print(formatter.format("-", "-", "+", "+"))
