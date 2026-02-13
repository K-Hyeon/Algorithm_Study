max_num = 0
row, column = 0, 0

for i in range(9):
  arr = list(map(int, input().split()))
  for j in range(9):
    if arr[j] > max_num:
      max_num = arr[j]
      row = i
      column = j
print(max_num)
print(f'{row+1} {column+1}') 