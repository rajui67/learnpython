import os

os.system('clear')
pets = {'dog': 'Bark', 'cat': 'Meow', 'parrot': 'Squawk'}


print('\nLoop over pets using enumerate(pets):')
for sound_pet_makes in enumerate(pets):
    print(sound_pet_makes)


    '''
    produces output:
    (0, 'dog')
    (1, 'cat')
    (2, 'parrot')
    '''
    

print('\nLoop over pets and  using pets[pet] to get the sound produced by the pet:')
for pet in pets:
    print(1, pet, 2, pets[pet]) # when you loop over a dict the value in the loop variable is the value of the key of the dict

    '''
    produces output:

    1 dog 2 Bark
    1 cat 2 Meow
    1 parrot 2 Squawk
    '''


print('\nLoop over pets and  using get(pet) to get the sound produced by the pet:')
for pet in pets:
    print(1, pet, 2, pets.get(pet))

    '''
    produces output:

    1 dog 2 Bark
    1 cat 2 Meow
    1 parrot 2 Squawk
    '''

print('\nLoop over pets using pets.values():')
for sound_pet_makes in pets.values():
    print(sound_pet_makes)

    '''
    produces output:
    Bark
    Meow
    Squawk
    '''
    
print('\nLoop over pets using pets.items():')
for (pet, sound_pet_makes) in pets.items():
    print(sound_pet_makes)

    '''
    produces output:
    Bark
    Meow
    Squawk
    '''

print('\nLoop over pets using enumerate(pets.values()):')
for counter, sound_pet_makes in enumerate(pets.values()):
    print(sound_pet_makes)

    '''
    produces output:
    Bark
    Meow
    Squawk
    '''

print('\nLoop over pets using enumerate(pets.items()):')
for i, (pet, sound_pet_makes) in enumerate(pets.items()):
    print(sound_pet_makes)

    '''
    produces output:
    Bark
    Meow
    Squawk
    '''
