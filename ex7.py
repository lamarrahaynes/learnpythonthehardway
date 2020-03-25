# This line displays "Mary had a alittle lamb in the  terminal"
print("Mary had a little lamb.")

""" This line displays "It's fleece was white as snow in the terminal."

The word "snow" is printed using the str.format(), which is one of the string formatting methods in Python 3. It allows multiple substitutions and value formatting. This method lets us concatenate elements within a string via positional formatting. Formatters work by putting in one or more replacement fields and placeholders defined by a pair of curly braces, {}, into a string and calling the str.format(). The value we wish to put into the placeholders and concatenate with the string are passed as parameters into the format function.

Syntax: {}.format(value)

Parameters:
(value) Can be an integer, float, string, characters, or even variables.

Outcome: A formatted string with the value passed as parameter in the placeholder position.

"""
# The period after the {} gets printed onto the screen the second period is a part of the format method.
print("Its fleece was white as {}.".format('snow'))
# Displays "And everywhere that Mary went" in the terminal
print("And everywhere that Mary went")
# I know the print(".") will display the "." onto the screen. adding the *10 multiples it by 10 and displays it the period 10 times on to the terminal
print("." * 10)
# Creates the variable end1 with the value of "C"
end1 = "C"
# Creates the variable end2 with the value of "h"
end2 = "h"
# Creates the variable end3 with the value of "e"
end3 = "e"
# Creates the variable end4 with the value of "e"
end4 = "e"
# Creates the variable end5 with the value of "s"
end5 = "s"
# Creates the variable end6 with the value of "e"
end6 = "e"
# Creates the variable end7 with the value of "B"
end7 = "B"
# Creates the variable end8 with the value of "u"
end8 = "u"
# Creates the variable end9 with the value of "r"
end9 = "r"
# Creates the variable end10 with the value of "g"
end10 = "g"
# Creates the variable end11 with the value of "e"
end11 = "e"
# Creates the variable end12 with the value of "r"
end12 = "r"

# watch end = '' at the end. try removing it to see what happens
# Outcome: Removing the end=' ' after end6 displays Cheese Burger on two lines instead of next to each other on one line
# Concatenates the values of the variables end1, end2, end3, end4, end5, and end6. Then adds a space after the concatenation w/ end=' '. Everything is then displayed onto the screen
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# Concatenates the values of the variables end7, end8, end9, end10, end11, and end12 and displays the outcome onto the screen.
print(end7 + end8 + end9+ end10 + end11 + end12)

# end=' ' is a parameter for the print() function. By default the value of this parameter is '\n', which is the new line character.You can end a print statement with any character/string using this parameter. By default python's print() function ends with a newline the end='' allows the print() function to stay on the same line

# In this example the end parameter has a value of '@' multipled by 8
# print(end1 + end2 + end3 + end4 + end5 + end6, end='@'*8)
