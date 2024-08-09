def trans_binary(n, num, board):
    for i in range(n-1, -1, -1):
        if board[n - i - 1] == '#': 
            num -= (num // (2**i)) * (2**i)
            continue
        if num // (2**i) == 1:
            board[n - i - 1] = '#'
        else: board[n - i - 1] = ' '
        num -= (num // (2**i)) * (2**i)
    return board

def solution(n, arr1, arr2):
    answer = []
    board = [[''] * n for _ in range(n)]
    for i in range(n):
        trans_binary(n, arr1[i], board[i])
        trans_binary(n, arr2[i], board[i])
        answer.append(''.join(board[i]))
    print(board)
    return answer