# 방법1
n = int(input())

n_5 = n//5
if n % 5 == 0:
    n_3 = 0
elif n % 5 == 1:
    n_5 -= 1
    n_3 = 2
elif n % 5 == 2:
    n_5 -= 2
    n_3 = 4
elif n % 5 == 3:
    n_3 = 1
elif n % 5 == 4:
    n_5 -= 1
    n_3 = 3
    
if n_5 < 0:
    print(-1)
else:
    print(n_5 + n_3)
    
# 방법2
n = int(input())

cnt = 0
while 1:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    
    n -= 3
    cnt += 1
    
    if n < 0:
        print(-1)
        break