#!/usr/bin/env python

# The else of the for clause does not run  if the for loop exits with a break
# as the for loop did not run its "natural" course.
import os
os.system("clear")
acceptable_values = list(range(10,101,10))
number_of_tries = len(acceptable_values)
hit_counter = 0
print(acceptable_values)

for (counter, throw_away) in enumerate(acceptable_values, start=1):
    user_entered_value = int(input("Please Enter an Integer Value: "))
    print(f"Value entered is {user_entered_value}")
    if user_entered_value in acceptable_values:
        hit_counter = hit_counter + 1
    if counter == number_of_tries and hit_counter != number_of_tries:
        print(f"Exiting! {'Only' if hit_counter else '' } {hit_counter} out of {number_of_tries} attempts matched")
        break
else:
    print(f"success! All {hit_counter} attempts out of {number_of_tries} attempts matched!")