#import sys
#input = sys.stdin.readline

m = int(input())

for i in range(1, m+1):
    print(' '*(m-i)+'*'*i)