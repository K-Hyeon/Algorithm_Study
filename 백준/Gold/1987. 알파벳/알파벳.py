R, C = map(int, input().split()) # 가로, 세로
board = [input() for _ in range(R)]

result = 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def Start(x, y):
    global result
    q = []
    q.append((x, y, board[x][y]))
    
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        
        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx) and (nx < R) and (0 <= ny) and (ny < C) and (board[nx][ny] not in step):
                q.append((nx, ny, step + board[nx][ny]))
    
Start(0, 0)
print(result)