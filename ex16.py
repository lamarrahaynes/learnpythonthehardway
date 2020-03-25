# From the sys module import the argv feature
from sys import argv

# These are the parameters to be given to the command line
script, filename = argv

# Prints the string below onto the terminal. Note the use of the f.string, string method, which ensures that the string prints with the name of the "filename" variable.
print(f"We're going to erase {filename}.")

# Prints the string below onto the terminal.
print("If you don't want that, hit CTRL-C (^C).")

# Prints the string below onto the terminal
print("If you do want that, hit RETURN.")

# Displays (prints) the "?" mark onto the screen
input("?")

# Prints the following string onto the terminal
print("Opening the file...")

# open() is a function that opens your text file, granted you passed, aka typed, the file name in the commandline. In this case it will open the file called "filename" The "w" means "write" So open the "filename," which was specified earlier in line 2 and write in it.
target = open(filename)


# Prints the follwing string onot the terminal
print("Truncating the file.  Goodbye!")

# Truncates or empties the file. BE CAREFUL. YOU CAN LOSE YOUR FILE.
target.truncate()

# Prints the followng string onto the terminal screen
print("Now I'm going to ask you for three lines.")

# Creates a variable called "line1." The value of "line1" is the input() funcion, which has the string value of "line 1: "
line1 = input("line 1: ")

# Creates a variable called "line2." The value of "line2" is the input() funcion, which has the string value of "line 2: "
line2 = input("line 2: ")

# Creates a variable called "line3." The value of "line3" is the input() funcion, which has the string value of "line 3: "
line3 = input("line 3: ")

# Prints the string below onto the terminal
print("I'm going to write these to the file.")

# The write("stuff") function, writes "stuff" to the file. In this case, the parameter of stuff is replaced with the variable "line1". The content of line1 is added to the target variable?
target.write(line1)

# Adds a new line to the target variable (\n)
target.write("\n")

# Adds "line2" to the target variable
target.write(line2)

# Adds a new line to the target variable (\n)
target.write("\n")

# Adds "line3" to the target variable
target.write(line3)

# Adds a new line (\n) to target variable after the "line3" addition
target.write("\n")

# Prints the string below to the terminal
print("And finally, we close it.")

# The close() function closes the file. Like File->Save...in your editor.
target.close()


# There’s too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
# Use concatenation to do this:
# target.write(line1 + "\n" + line2 + "\n" + line3)
