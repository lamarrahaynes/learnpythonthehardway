# Says from the sys(system) module import the argv(argument variable) feature.
# The purpose of a rgv is to get command line arguments from a user. It is another way to get user input, like the input() function.
# In other words argv is "argument variable" that holds variables that you send (aka pass) to Python
# input() and argv vary in where they get user input from. input() accepts user data from inside a running program and argv accepts user data from within the command line prompt.
from sys import argv
# read the WYSS section for how to run this

# This line unpacks argv into 4 variables from left to write starting with "script."
script, first, second, third = argv

# Prints the sentence "The script is called: ex13.py" because the first argument, which is by default always the name of the script is the first argument typed ou => python ex13.py
print("The script is called:", script)

# Prints the sentence "Your first variable is: "name of argument given""
# If you set the argument to be "table" the following would be printed: "Your first variable is: table"
# So the value of your first variable => "table"
print("Your first variable is:", first)

# See note starting on line 13
print("Your second variable is:", second)
# See note starting on line 13
print("Your third variable is:", third)


# With fewer than 3 arguments, say 2, you will get a an value error that will say something like this:
# "Value Error: not enough values to unpack expected 4, got 2" Thre are only two arguments, but four
# arguements are needed to run the code
# always the first argument, and "table" is the second.
# When there are too many scripts the following error message is displayed: "Value error: too many values to unpack (expected 4)"
