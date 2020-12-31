t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    dist = y - x
    
    l_sqrt = int(dist**(1/2))
    u_sqrt = l_sqrt + 1
    
    if dist == l_sqrt**2:
        print(l_sqrt*2-1)
    elif dist <= u_sqrt**2 -u_sqrt:
        print(l_sqrt*2)
    else:
        print(u_sqrt*2-1)