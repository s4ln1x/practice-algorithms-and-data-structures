#!/usr/bin/env python3

# Advantages of using arrays:
#
#    Arrays allow random access of elements. This makes accessing elements by position
#    faster.
#    Arrays have better cache locality that can make a pretty big difference in
#    performance.

import array
import time

NUMBER_OF_ELEMENTS = 10000000
# Create array and list
MY_ARRAY = array.array('i', range(NUMBER_OF_ELEMENTS))
MY_LIST = list(range(NUMBER_OF_ELEMENTS))

def completionTime(func):
    """
    Measures the time another function take to execute
    """
    def decorated():
        start = time.time()
        func()
        duration = time.time() - start
        print('{} took {} seconds to finish'.format(func.__name__, duration))

    return decorated


@completionTime
def iterateArray():
    """
    Iteration over an array
    """
    for i in MY_ARRAY:
        pass


@completionTime
def iterateList():
    """
    Iteration over a list
    """
    for i in MY_LIST:
        pass


def main():
    """
    Main function
    """
    iterateList()
    iterateArray()


if __name__ == '__main__':
    main()

# It seems lists are faster in python than arrays maybe python is using something
# special for lists
