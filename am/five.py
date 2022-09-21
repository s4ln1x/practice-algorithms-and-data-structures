#!/usr/bin/env python3

def solution(N):
    # write your code in Python 3.6

    # Review if N is positive or negative
    is_N_positive = True if N > 0 else False

    # Making the integer a list
    list_N = list(str(N)) if is_N_positive else str(N[1:]).split()

    # These numbers lists are to know how 5 compares against the other digits
    lower_numbers = ['0', '1', '2', '3', '4', '5'] if is_N_positive else ['5', '6', '7', '8', '9']

    # Reviewing all the possible values
    for i in range(len(list_N)):

        # Add the '5' digit to the left
        if list_N[i] in lower_numbers:
            list_N.insert(i, '5')
            break

    else:

        # Add the '5' digit to the last position to the right
        list_N.insert(i, '5')

    # Make the list a number again
    max_number = int("".join(list_N))

    return max_number


if __name__ == "__main__":
    print(solution(268))
