def Solution(N):
    """This function is for solve the task 1"""
    for number in range(1, N + 1):
        word_numbers = {2: 'Codibility', 3: 'Test', 5: 'Coder'}
        word = ''
        for k in word_numbers.keys():
            if number % k == 0:
                word += word_numbers[k]
        if word:
            print(word)
        else:
            print(number)


print('With 21, the result is:')
Solution(21)
print('With 5, the result is:')
Solution(5)
print('With 7, the result is:')
Solution(7)
print('With 15, the result is:')
Solution(15)
