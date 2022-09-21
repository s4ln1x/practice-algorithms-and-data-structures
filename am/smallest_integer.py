#!/usr/bin/env python3


# Find the smallest positive integer that does not occur in a given sequence.

def solution(A):
    # write your code in Python 3.6
    # Positive integer
    A = sorted(list(set(filter(lambda x: x if x > 0 else None, A))))

    # All number are negative return 1
    if A == []:
        smallest_number = 1

    # A is a perfect sequence
    elif len(A) == A[-1]:
        smallest_number = A[-1] + 1

    # Smallest number
    else:
        for i in range(1, A[-1] + 1):
            if i not in A:
                smallest_number = i
                break

    return smallest_number


if __name__ == "__main__":
    import random

    magic_numbers = list()

    for _ in range(1000000):
        magic_numbers.append(random.randint(-1000000, 1000000))

    print(solution(magic_numbers))
