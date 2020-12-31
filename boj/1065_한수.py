#import sys
#input = sys.stdin.readline

def hansu(n):
    result = 0
    if n < 100:
        result = 1
    elif n == 1000:
        result = 0
    elif 2*(n%100//10) == n//100 + n%10:
        result = 1
    return result

cnt = 0
for i in range(1, int(input())+1):
    if hansu(i) == 1:
        cnt+= 1
        
print(cnt)