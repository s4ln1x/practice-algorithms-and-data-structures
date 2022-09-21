# Task 1

Given any number N, print all the numbers from 1 to N, if the number is 
divisible between 2, 3 or 5 instead of printing the number.
You should print the following strings: "Codility", "Test", "Coder" respectively,
also you need to take into consideration that the strings need to be printed 
in order.
Also, if the number is divisible by two or three of the numbers at the same
time you need to concatenate the string.

    "CodilityTestCoder"
    "TestCoder"
    "CodilityCoder"
    Etc
    
    Example:
    N = 15
    1
    Codility
    Test
    Codility
    Coder
    CodilityTest
    7
    Codility
    Test
    CodilityCoder
    11
    CodilityTest
    13
    Codility
    CodilityTestCoder