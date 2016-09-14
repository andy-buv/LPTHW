# Assigns 'cars' with integer 100
cars = 100
# Assigns 'space_in_a_car' with float 4.0
space_in_a_car = 4.0
# Assigns 'drivers' with integer 30
drivers = 30
# Assigns 'passengers' with integer 90
passengers = 90
# Assigns 'cars_not_driven' with the integer calculated from calling 'cars' - 'drivers'
cars_not_driven = cars - drivers
# Assigns 'cars_driven' with the same value as 'drivers'
cars_driven = drivers
# Assigns 'carpool_capacity' with the calculated product of 'cars_driven' and 'space_in_a_car'
carpool_capacity = cars_driven * space_in_a_car
# Assigns 'average_passengers_per_car' with calculated value 
average_passengers_per_car = passengers / cars_driven

# Prints "There are" inserts 'cars' value, prints " cars available."
print "There are", cars, "cars available."
# Prints "There are only" inserts 'drivers' value, prints " drivers available."
print "There are only", drivers, "drivers available."
# Prints "There will be" inserts 'cars_not_driven' value, prints " empty cars today."
print "There will be", cars_not_driven, "empty cars today."
# Prints "We can transport" inserts 'carpool_capacity' value, prints " people today."
print "We can transport", carpool_capacity, "people today."
# Prints "We have" inserts 'passengers' value, prints " to carpool today."
print "We have", passengers, "to carpool today."
# Prints "We need to put about" inserts 'average_passengers_per_car' value, prints " in each car."
print "We need to put about", average_passengers_per_car, "in each car."

"""
When I wrote this program the first time I had a mistake, and Python told me about it like this:

Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

Explain this error in your own words. Make sure you use line numbers and explain why.

'car_pool_capacity is not defined. whereas carpool_capacity is. 
Therefore there is an error in trying to calculate.
"""