#!/usr/bin/env python3

def solution(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            break
    else:
        i = i + 1

    return s[:i] + s[i + 1:]


if __name__ == "__main__":
    print(solution("abc"))
    print(solution("hot"))
    print(solution("codibility"))
    print(solution("cooudibility"))
    print(solution("aaaa"))
