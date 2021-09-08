#import sys
#input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    parents  = [0] * (N+1)
    for _ in range(N-1):
        p, c = map(int, input().split())
        parents[c] = p
    
    a, b = map(int, input().split())
    
    a_parents = set()
    a_parents.add(a)
    
    while parents[a]:
        a = parents[a]
        if a == b:
            print(a)
            break
        a_parents.add(a)

    while parents[b]:
        b = parents[b]
        if b in a_parents:
            print(b)
            break
