# 정답 -> bfs
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1

# 상하좌우
dy = [-1, 1, 0, 0] 
dx = [0, 0, -1, 1]

queue = deque()
queue.append((0,0))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[y][x] + 1
                queue.append((ny, nx))

print(visit[N-1][M-1])