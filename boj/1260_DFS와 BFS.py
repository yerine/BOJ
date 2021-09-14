#import sys
#input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())

graph = {}
for i in range(m):
    a, b = map(int, input().split())
    
    if a not in graph:
        graph[a] = [b]
    elif a in graph:
        graph[a].append(b)
        
    if b not in graph:
        graph[b] = [a]
    elif b in graph:
        graph[b].append(a)
        
def dfs(graph, v=v):
    visit=[]
    stack=[v]
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph:
                stack.extend(sorted(graph[node], reverse=True))
            
    print(" ".join(map(str, visit)))

def bfs(graph, v=v):
    visit = []
    queue = deque([v])
    
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in graph:
                queue.extend(sorted(graph[node]))
        
    print(" ".join(map(str, visit)))

dfs(graph)
bfs(graph)