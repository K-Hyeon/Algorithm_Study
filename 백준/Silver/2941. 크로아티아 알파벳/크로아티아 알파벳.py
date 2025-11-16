text = input()
board = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(board)):
    text = text.replace(board[i], 'c')
print(len(text))