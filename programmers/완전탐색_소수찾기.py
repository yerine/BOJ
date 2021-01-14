from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    answer = set()

    for i in range(1,len(numbers)+1):
        for number in set(int("".join(p)) for p in permutations(numbers,i)):

            if number > 1:
                prime = True
                for quot in range(2, number):
                    if number % quot == 0:
                        prime = False
                        break
                if prime == True:
                    answer.add(number)

    return len(answer)

from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    answer = set()

    for i in range(1,len(numbers)+1):
        for number in set(int("".join(p)) for p in permutations(numbers,i)):

            if number > 1:
                prime = True
                for quot in range(2, int(number**0.5) + 1):
                    if number % quot == 0:
                        prime = False
                        break
                if prime == True:
                    answer.add(number)

    return len(answer)

# 다른 사람의 풀이

from itertools import permutations

def solution(numbers):
    answer  = set()
    
    for i in range(len(numbers)):
        answer |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    answer -= set(range(0, 2))
    
    for i in range(2, int(max(answer) ** 0.5) + 1):
        answer -= set(range(i * 2, max(answer) + 1, i))
        
    return len(answer)