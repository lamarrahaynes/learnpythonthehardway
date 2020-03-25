# The line below creates the variable types_of_people and it has value of 10 n
types_of_people = 10
# This creates the variable x. The value of x is format string, which combines
# the string "There are types of people" with the variable types_of_people
x = f"There are {types_of_people} types of people."
# This creates the variable binary with the string value of binary
binary = "binary"
# This creates the varaiable do_not with the string value of don't
do_not = "don't"
# This creates the variable y. The value of which is a format string.
# Combining the string "Those who know and thos who" with the variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."
# displays the value of the variable x in the terminal
print(x)
# displays the value of the variable y in the terminal
print(y)
# This prints the format string. This f string combines the string "I said" w/ the variable x
print(f"I said {x}")
# This prints the format string. This f string combines
print(f"I also said: '{y}' ")
# Creates the variable hilarious with a value of False
hilarious = False
# Creates the variable joke_evaluation with the string value seen below.
joke_evaluation = "Isn't that joke so funny?! {}"
# displays the values of the joke_evaluation and hilarious in a sentence
print(joke_evaluation.format(hilarious))

# Creates the variable w with a string as its value
w = "This is the left side of..."
# Creates the variable e with a string as its value
e = "a string with a right side."
# dispays the values of variables w and e printed in a sentence 
print(w + e)
