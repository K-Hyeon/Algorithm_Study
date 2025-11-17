from collections import deque

N = int(input())
M = int(input())

board = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visit = [False] * (N+1)
visit[1] = True

answer = 0
queue = deque()
queue.append((1))
while queue:
    temp = queue.popleft()
    for i in board[temp]:
        if visit[i]==False:
            queue.append(i)
            visit[i] = True
            answer += 1
print(answer)        