# from exercise 5 height = 74 inches
height = 74 * 2.54
print(height)

# from exercise weight = 180 lbs

# / division produces a float
weight = 180 / 2.205
# // division produces an integer
# weight = 180 / 2.205  produces a float up to the exact decimal
# weight = 180 // 2.205 produces a float with one decimal becasue double slash
# division only produces an integer, but the integer 180 is being divided by the float 2.205 so it produces an float, but only with one decimal place.
new_weight = 180 // 2.205

# use the round() function to round a number.
rounded_weight = round(weight)


print(weight)
print(new_weight)
print(rounded_weight)
