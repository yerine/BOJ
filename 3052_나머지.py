#import sys
#input = sys.stdin.readline

lst = list()
for i in range(10):
    num = int(input())
    num %= 42
    if num not in lst:
        lst.append(num)
        
print(len(lst))