# 방법1
n = int(input())
while n != 0:
    arr = [False] + [True]*(2*n-1)
    for i in range(2, int((2*n)**0.5+1)):
        if arr[i-1]:
            for j in range(2*i, 2*n+1, i):
                arr[j-1] = False
    print(sum(arr[n:]))
    
    n = int(input())
    
#방법2
arr = [False] + [True]*(2*123456-1)
for i in range(2, int((2*123456)**0.5+1)):
    if arr[i-1]:
        for j in range(2*i, 2*123456+1, i):
            arr[j-1] = False

n = int(input())
while n != 0:
    print(sum(arr[n:2*n]))    
    n = int(input())

