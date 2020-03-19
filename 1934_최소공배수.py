#import sys
#input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split())
    c = a*b
    
    while b:
        a, b = b, a%b
        
    print(int(c/a))