from collections import deque

#하좌상우, L=-1, R=+1
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
def move(y, x, r):
    global board
    if move_info:
        temp = move_info.popleft()
        if temp == 'R':
            r = (r+1)%4
            move(y, x, r)
        elif temp =='L':
            r = (r+3)%4
            move(y, x, r)
        else:
            y += dy[r]
            x += dx[r]
            board[y][x] = '.'
            move(y,x,r)

N = int(input())
move_info = deque(list(map(str,input().strip())))

board = [['#']*101 for _ in range(101)]
board[50][50] = '.'

move(50, 50, 0)

max_x, min_x, max_y, min_y = 0, 1e9, 0, 1e9
for i in range(101):
    for j in range(101):
        if board[i][j] == '.':
            if min_y > i: min_y = i
            if max_y < i : max_y = i
            if min_x > j : min_x = j
            if max_x < j : max_x = j

for i in range(min_y, max_y+1):
    print("".join(board[i][min_x:max_x+1]))
