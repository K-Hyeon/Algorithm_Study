import sys
input = sys.stdin.readline

board = list(map(int, input().split()))

index20 = board.index(20)
Alice_score = (board[index20-1] + board[index20] + board[(index20+1)%20])/3
Bob_score = sum(board)/20

if Alice_score < Bob_score: print('Bob')
elif Alice_score == Bob_score: print('Tie')
else: print('Alice')