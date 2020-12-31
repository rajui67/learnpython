#!/usr/bin/env python
import os
os.system("clear")

for counter in range(10):
    print(f"counter value = {counter}")
    integer_value = int(input("Please enter an integer: "))
    if integer_value < 0:
       print(f"Integer {integer_value} is less than 0")
    elif integer_value == 0:
       print("Integer value is 0")
    else:
       print(f"integer {integer_value} is greater than 0")
    