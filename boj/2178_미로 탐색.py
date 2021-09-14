#import sys
#input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

maze = [input() for _ in range(n)]

visit = [[0]*m for _ in range(n)]
visit[0][0] = 1
dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]

queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and maze[nx][ny] == '1':
            queue.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1
            
print(visit[-1][-1])
        
