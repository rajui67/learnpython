from all_decorators import decoratator_with_ability_to_pass_parameters_and_return_values
'''
'''

@decoratator_with_ability_to_pass_parameters_and_return_values
def example(message, message1, message2):
    print(message, message1, message2, sep="\n")
    return "Printed Successfully"

print(example(11, 12, message2=13))