from repeater import Repeater

counter = 0
for iteration in Repeater('abc'):
    print(iteration)
    counter += 1
    if counter == 3:
        break
