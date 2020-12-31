#import sys
#input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split(' ')))

m = max(scores)
scores = [i/m*100 for i in scores]

print(sum(scores)/n)
    