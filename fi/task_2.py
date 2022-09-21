def Solution(A):
    A = sorted(set(A))
    for i in range(len(A) - 1):
        if A[i] - A[i + 1] == -1:
            return True
    else:
        return False


print(Solution([7]))
print(Solution([3, 7, 8, 4]))
print(Solution([5, 5, 5, 5]))
print(Solution([1, 3, 9, 76, 34, 20, 13, 12]))
