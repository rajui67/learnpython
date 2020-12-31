import os
'''
Denonstrates that function/method parameters dont have a specific type in Python.  
'''


class Demo:
    """Models a Demo."""

    def __init__(self, demo_parameter: list):
        """Demo Class Constructor to initialize the object.

        Input Arguments:  demo_parameter: must be list. 
        """
        self.data_member = demo_parameter


os.system("clear")

# In this invoication of the constructor, demo is an object instance whose data_member is a list type.
# (Each element of the list is a dict)
demo = Demo([{"name": "carrots", "quantity": 10}, {
    "name": "peas", "quantity": 200}])

# append is a method to add an element to a list
demo.data_member.append({"name": "cucumber", "quantity": 10})

print(demo.data_member)
for item in demo.data_member:
    print(item, item["name"], item["quantity"])


# In this invoication of the constructor, demo is an object instance whose data_member is a dict type.
demo = Demo({"name": "carrots", "quantity": 10})
demo.data_member["taste"] = "bitter"
print(demo.data_member, demo.data_member["name"],
      demo.data_member["quantity"])

# In this invoication of the constructor, demo is an object instance whose data_member is a str type.
demo = Demo("apple")
print("\ncondiment is a simple variable\n")
print(demo.data_member)

# In this invoication of the constructor, demo is an object instance whose data_member is a tuple type.
demo = Demo(("carrots", "peas", "cucumber", "tomato", "potato"))
print(demo.data_member)
for item in demo.data_member:
    print(item)

# In this invoication of the constructor, demo is an object instance whose data_member is a set type.
demo = Demo({"carrots", "peas", "cucumber", "tomato", "potato"})
demo.data_member.add("okra")
print(demo.data_member)
for item in demo.data_member:
    print(item)
