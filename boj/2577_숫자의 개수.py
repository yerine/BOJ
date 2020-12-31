#import sys
#input = sys.stdin.readline

num = 1
for i in range(3):
    num *= int(input())

num = str(num)

for i in range(10):
    print(num.count(str(i)))