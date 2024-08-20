import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input() for _ in range(R)]

answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(arr, x, y):
    global answer
    if answer == 26: return
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C) and (board[nx][ny] not in arr):
            dfs(arr + board[nx][ny], nx, ny)
        else:
            answer = max(answer, len(arr))

arr = board[0][0]
dfs(arr, 0, 0)
print(answer)
