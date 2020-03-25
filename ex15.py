""# From the system module import the argv (argument variable) feature
from sys import argv

# The argument variable has 2 values script, the name of the script (in this case ex.15.py) and filename (in this case ex15_sample.txt).
# The name of the "script" and the name of the "filename" will be the arguments passed in the command line3
# The arguments are passed from the command line into the python program.
# THis is what you type in the terminal: python ex15.py ex15_sample.txt
script, filename = argv

# Creates a variable called "txt" with
# The value of the "txt" variable is: open(filename).
# open() is a function that opens your text file, granted you passed, aka typed, the file name in the commandline
txt = open(filename)

# Prints the following message using the f string onto the terminal.
# The message will look like this: "Here's your ex15_sample.txt:"
print(f"Here's your {filename}:" )

# txt is the variable or object
# the "." (dot) is to add a function or command, in this case read. As in read the "txt" variable
print(txt.read())
""
# The lines below do everything you just did above, except w/in the script (using the input() function instead of argv)
# Prints the following message onto the terminal
print("Type the filename again:")
# Creates a variable called file_again
# The value of file_again is: input("> ")
file_again = input("> ")

# Creates a variable called txt_again
# The value of txt_again is: open(file_again)
# open() will open the ex15_sample.txt file
txt_again = open(file_again)

# Says read the txt_again file and print the file onto the screen
print(txt_again.read())

# You need to close the files. 
txt.close
txt_again.close
