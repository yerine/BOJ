#import sys
#input = sys.stdin.readline

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print("Case #%s: %s + %s = %s"%(i+1, a, b, a+b))