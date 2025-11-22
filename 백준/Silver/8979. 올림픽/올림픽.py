N, K = map(int, input().split()) #N=국가 수, K=등수를 알고 싶은 국가
board = [list(map(int, input().split())) for _ in range(N)]

board.sort(key=lambda x: (-x[1], -x[2], -x[3]))

answer = 1
if board[0][0] == K : print(answer)
else:
    for i in range(1, N):
        if board[i-1][1:] != board[i][1:]:
            answer += 1
        if board[i][0] == K:
            print(answer)
            break