#import sys
#input = sys.stdin.readline

arr = [False] + [True]*(10000-1)
for i in range(2, int((10000)**0.5+1)):
    if arr[i-1]:
        for j in range(2*i, 10000+1, i):
            arr[j-1] = False
            
t = int(input())

for i in range(t):
    n = int(input()) 
    for j in range(n//2, 1, -1):
        if arr[j-1] == True and arr[n-j-1]:
            print(j, n-j)
            break