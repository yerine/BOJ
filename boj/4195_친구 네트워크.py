#import sys
#input = sys.stdin.readline

n = int(input())

def find(target):
    if parents[target] == target:
        return target
    
    parents[target] = find(parents[target])
    return parents[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
        counts[a] += counts[b]
        counts[b] = 0
    elif a > b:
        parents[a] = b
        counts[b] += counts[a]
        counts[a] = 0
    
for _ in range(n):
    parents = {}
    counts = {}
    f = int(input())
    for _ in range(f):
        a, b = input().split()
        if a not in parents:
            parents[a] = a
            counts[a] = 1
        if b not in parents:
            parents[b] = b
            counts[b] = 1
            
        union(a, b)
        print(parents)
        print(counts)
        print(counts[find(a)])
        