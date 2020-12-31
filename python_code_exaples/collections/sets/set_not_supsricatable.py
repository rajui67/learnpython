import os

os.system("clear")

set_of_condiments = {"carrots", "peas", "cucumber", "tomato", "potato"}
print(set_of_condiments)
for item in set_of_condiments:
    print(item)

print(len(set_of_condiments))

'''will genereate error 'set' object is not subscriptable'''
print(set_of_condiments[0])

