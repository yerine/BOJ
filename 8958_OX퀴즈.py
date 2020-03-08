#import sys
#input = sys.stdin.readline

n = int(input())

for i in range(n):
    result = input()
    score = 0
    cnt = 0
    for i in result:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)