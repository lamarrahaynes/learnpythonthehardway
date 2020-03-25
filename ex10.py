# Creates a variable called tabby_cat. The use of the \t escape key tabs the variable's value in to the right.
tabby_cat = "\tI'm tabbed in."

# Creates a variable called persian_cat. The use of the \n escape key prints the "on a line." portion of the value onto a new line, seperate from "I'm split"
persian_cat = "I'm split\non a line."

# Creates a variable called backslash_cat. The use of \\ escape key prints a "\" between "I'm" and "a" and another backslash between "a" and "cat"
backslash_cat = "I'm \\ a \\ cat."

# Creates a variable called fat_cat whose value is the string below. The use of the triple quotes allows you to make the string as long as you want. The first 3 list items ("Cat food", "Fishies", and "Catnip") are all tabbed in to the right. The last item "Grass" is on a new line, below "Catnip" and is also tabbed in to the right.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass'''

# Prints the value of the tabby_cat varible onto the terminal.
print(tabby_cat)
# Prints the value of the persian_cat variable onto the terminal.
print(persian_cat)
# Prints the value of the backslash_cat variable onto the terminal.
print(backslash_cat)
# Prints the value of the fat_cat variable onto the terminal.
print(fat_cat)

print( "I screamed, \"He's going to kill me!\"")
print ('\rI screamed, "He\'s going to kill me!"')
