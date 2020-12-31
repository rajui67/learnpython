def numberGenerator(number):
    #  number = yield
    number = 0
    while number < number:
        i = yield number 
        if i is not None:
            number = i
        else:        
            number += 1

generator = numberGenerator(10)    # Create our generator
print(next(generator))         
print(next(generator))              # 
print(next(generator))         
print(generator.send(5))