t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
        
    dis = (x1-x2)**2 + (y1-y2)**2
    r_sum = (r1 + r2)**2
    r_diff = (r1 - r2)**2
    
    if dis > r_sum or dis < r_diff:
        print(0)
    elif dis == r_sum or dis == r_diff:
        print(1)
    else:
        print(2)