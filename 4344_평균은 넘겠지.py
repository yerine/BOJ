#import sys
#input = sys.stdin.readline

c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    n = scores.pop(0)
    avg = sum(scores)/n
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    print("%.3f%%"%round(cnt/n*100,3))