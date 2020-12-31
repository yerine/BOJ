#import sys
#input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for i in range(n)]

numbers.sort()

for i in numbers:
    print(i)
    
#Bubble Sort
n = int(input())
numbers = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(n-1,i,-1):
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            
for i in numbers:
    print(i)
    
#Insertion Sort
n = int(input())
numbers = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(n-1,i,-1):
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            
for i in numbers:
    print(i)