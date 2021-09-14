#import sys
#input = sys.stdin.readline

n = int(input())     # 도시의 수
m = int(input())     # 여행 계획에 속한 도시들의 수 

parents = list(range(n))

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parents[b] = a
        
def find(target):
    if parents[target] == target:
        return target
    
    parents[target] = find(parents[target])
    return parents[target]

for city1 in range(n):
    route = list(map(int, input().split()))
    for city2 in range(city1, n):
        if route[city2] == 1:
            union(city1, city2)

plans = list(map(int, input().split()))
parent = find(plans[0]-1)

answer = "YES"
for plan in plans[1:]:
    if parent != find(plan-1):
        answer = "NO"
        break

print(answer)