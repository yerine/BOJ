n = int(input())
num_list = list(map(int, input().split()))

cnt = n
for i in num_list:
    if i == 1:
        cnt -= 1
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt -= 1
                break
            
print(cnt)