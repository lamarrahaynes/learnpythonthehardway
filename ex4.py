# Cars variable equals 100
cars = 100

# space_in_a_car equals 4
space_in_a_car = 4

# drivers variable = 30
drivers = 30

# passengers variable equals 90
passengers = 90

# cars_not_driven variable equals cars variable subtract drivers variable
# So cars_not_driven = 100 - 30 which equals 70
# cars_not_driven = 70
cars_not_driven = cars - drivers

# cars_driven variable equals drivers varialbe
# So cars_driven = 30
cars_driven = drivers

# carpool_capacity equals cars_driven variable mulitplied by space_in_a_car variable
# So carpool_capacity = 30 * 4 which equals 120
# carpool_capacity = 120
carpool_capacity = cars_driven * space_in_a_car

# average_passengers_per_car = passengers variable divided by cars_driven variable
# average_passengers_per_car = 90 / 30 which equals 3.0
#average_passengers_per_car = 3.0 because single slash division (/) always yields a float point number as its quotient
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")
