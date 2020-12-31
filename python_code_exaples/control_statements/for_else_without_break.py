#!/usr/bin/env python

# The else of the for clause runs after the for loop is exhausted
#!/usr/bin/env python

import os
os.system("clear")
acceptable_values = list(range(10,101,10))
number_of_tries = len(acceptable_values)
hit_counter = 0
print(acceptable_values)
for (just_for_looping, throw_away) in enumerate(acceptable_values, start=1):
    user_entered_value = int(input("Please Enter an Integer Value: "))
    print(f"Value entered is {user_entered_value}")
    if user_entered_value in acceptable_values:
        hit_counter = hit_counter + 1
else:
    print(f"completed. Values you entered matched expected values {hit_counter} out of {number_of_tries} times")