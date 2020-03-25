# Prints "How old are you?" onto the terminal. The end=''(which is a parameter for the print function) ensures that a new line isn't added after the print statement. So, the user input is written next to the print statement instead of the the user input going below the print statement, which is the defualt, see ex7 for more about end=''
print("How old are you?", end='')

# Asks the user to input or type in a value for their age
age = input()

# Prints "How tall are you?" onto the terminal. The end=''(which is a parameter for the print function) ensures that a new line isn't added after the print statement. So, the user input is written next to the print statement instead of the the user input going below the print statement, which is the defualt.
print("How tall are you?", end='')
# Asks the user to input a value for their height
height = input()

# Prints "How much do you weigh?" onto the terminal. The end=''(which is a parameter for the print function) ensures that a new line isn't added after the print statement. So, the user input is written next to the print statement instead of the the user input going below the print statement, which is the defualt.
print("How much do you weigh?", end='')

# Asks the user to input a value for their weight
weight = input()

# Uses the fstring string method to print "So, you're {age} old, {height} tall and {weight} heavy." By using the fstring the users inputs for age, height, and weight are entered into the string.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
