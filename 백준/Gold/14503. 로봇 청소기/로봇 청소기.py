# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def move(y, x, d):
    global answer

    # 1) 현재 위치 청소
    if board[y][x] == 0:
        board[y][x] = 2
        answer += 1

    # 2) 왼쪽부터 4칸 탐색
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 회전
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
            move(ny, nx, d)
            return

    # 3) 네 방향 모두 못 갔으면 후진
    back_d = (d + 2) % 4
    ny = y + dy[back_d]
    nx = x + dx[back_d]

    # 후진 가능할 때만 이동
    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != 1:
        move(ny, nx, d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
move(r, c, d)
print(answer)
