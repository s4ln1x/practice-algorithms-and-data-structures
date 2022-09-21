#!/usr/bin/env python3

import copy

numbers = [1, 2, 1, 4, -5, -7, 0, 100, 2000, -1234]

print(numbers)

# ANY OF THE BELOW SOLUTIONS WORKS FOR THIS EXERCISE

#for elt in numbers[:]:
#    # Could be any condition here
#    if True:
#        numbers.remove(elt)

#temp = copy.copy(numbers)
#for elt in temp:
#    # Could be any condition here
#    if True:
#        numbers.remove(elt)

#temp = copy.deepcopy(numbers)
#for elt in temp:
#    # Could be any condition here
#    if True:
#        numbers.remove(elt)

#for elt in reversed(numbers):
#    # Could be any condition here
#    if True:
#        numbers.remove(elt)

#numbers = [numbers.remove(elt) for elt in numbers if not True]

temp = []
for elt in reversed(numbers):
    # Could be any condition here
    if not True:
        temp.append(elt)
numbers = temp


print(numbers)
