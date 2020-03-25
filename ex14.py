# From the system modulue import the argv feature
from sys import argv
# Assigns two variables to argv
script, user_name = argv
# Creates variable called prompt with value of ">"
prompt = '**** '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"What color is your {computer}?")
computer_color = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer and it is {computer_color}. Nice.
""")
