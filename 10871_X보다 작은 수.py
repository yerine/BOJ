#import sys
#input = sys.stdin.readline

n, x = map(int, input().split())
lst = [i for i in input().split() if int(i) < x]
print(" ".join(lst))