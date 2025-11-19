len_board = int(input())
board = list(map(int, input().split()))
students = int(input())

for i in range(students):
    info, num = map(int,input().split())
    num -= 1
    if info == 1: #남학생
        for j in range(num, len_board, num+1):
            if board[j] == 0: board[j] = 1
            elif board[j] == 1: board[j] = 0
    if info == 2: #여학생
        # 해당 위치는 반대로 변경
        if board[num] == 0: board[num] = 1
        elif board[num] == 1: board[num] = 0
        # 그 외 위치 탐색
        for j in range(1, len_board):
            if 0 <= (num-j) and (num+j) < len_board: #이동 가능
                if board[num-j] == board[num+j]: # 숫자가 같다면 변경
                    if board[num-j] == 0: board[num-j] = board[num+j] = 1
                    elif board[num - j] == 1: board[num - j] = board[num + j] = 0
                else: break #숫자 다름
            else: break # 이동 불가
for i in range(1, len_board+1):
    if i % 20 == 0 or i == len_board:
        print(board[i-1])
    else: print(board[i-1], end=" ")

