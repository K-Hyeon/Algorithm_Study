# bfs
from collections import deque

def move(y, x):
    queue = deque()
    queue.append((y, x))
    visit[y][x] = 1
    count = 1

    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    queue.append((ny, nx))
                    count += 1
    return count


N = int(input())
board = [list(map(int, input().strip())) for i in range(N)]
visit = [[0]*N for _ in range(N)]

dy = [1, -1 , 0, 0]
dx = [0, 0, -1, 1]

result = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and visit[y][x] == 0:
            cnt = move(y, x)
            result.append(cnt)

result.sort()
print(len(result))
for r in result:
    print(r)