#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())

parents = list(range(n+1))

def find(target):
    '''find parent'''
    if target == parents[target]:
        return target
    
    return find(parents[target])

for _ in range(m):
    calc, a, b = map(int, input().split())
    if a == b:
        if calc == 1:
            print("YES")
        continue
    
    a = find(a)
    b = find(b)
    if calc == 0:
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
    else:
        if a == b:
            print("YES")
        else:
            print("NO")