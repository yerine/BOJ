t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    
    if k == 0:
        print(n)
        break
    
    cnt_lst = [i+1 for i in range(n)]
    for i in range(k-1):
        cnt_lst = [sum(cnt_lst[:i+1]) for i in range(n)]

    print(sum(cnt_lst))