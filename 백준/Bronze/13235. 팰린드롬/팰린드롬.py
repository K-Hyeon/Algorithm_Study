board = input()
n = len(board)

if n % 2 == 0: #짝수
    front = board[:n//2]
    end = board[n//2:]
else:
    front = board[:n // 2]
    end = board[n // 2 + 1:]
if front == end[::-1]: print("true")
else: print("false")