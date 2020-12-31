def factorial(n):
    result = 1
    for i in range(n):
        result *= i+1
    return result 

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))
