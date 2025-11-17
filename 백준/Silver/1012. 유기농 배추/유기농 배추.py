import sys
sys.setrecursionlimit(10**7)

dy = [1, -1 , 0, 0]
dx = [0, 0, -1, 1]

def check(y, x):
    global visit
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M: # 이동 가능
            if visit[ny][nx] == 0 and board[ny][nx] == 1: # 배추, 첫 방문
                visit[ny][nx] = 1
                check(ny, nx)

T = int(input())
for test_case in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    visit = [[0]*M for _ in range(N)]

    answer = 0
    for row in range(N):
        for column in range(M):
            if visit[row][column] == 0 and board[row][column] == 1:
                answer += 1
                check(row, column)
                    
    print(answer) 