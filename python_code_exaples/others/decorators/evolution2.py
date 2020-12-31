from all_decorators import decoratator_with_ability_to_pass_parameters
'''
'''

@decoratator_with_ability_to_pass_parameters
def example(message, message1, message2):
    print(message, message1, message2, sep="\n")

example(11, 12, message2=13)