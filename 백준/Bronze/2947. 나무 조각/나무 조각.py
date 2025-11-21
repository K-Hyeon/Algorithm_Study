def print_board():
    for j in range(5):
        if j == 4:
            print(board[j])
        else: print(board[j], end=" ")


board = list(map(int, input().split()))

while board != [1,2,3,4,5]:
    for i in range(4):
        if board[i] > board[i+1]:
            temp = board[i]
            board[i] = board[i+1]
            board[i+1] = temp
            print_board()