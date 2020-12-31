#!/usr/bin/env python

import os
os.system("clear")
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(type(enumerate(seasons)))
for index, value in enumerate(seasons):
    print(f"Index = [{index}] Value = [{value}]")
for index, value in enumerate(seasons, start=1):
    print(f"Index = [{index}] Value = [{value}]")
