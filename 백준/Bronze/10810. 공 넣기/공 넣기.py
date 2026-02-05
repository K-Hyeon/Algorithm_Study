N, M = map(int, input().split())
array = ['0']*N

for i in range(M):
  i, j, k = map(int, input().split())
  for num in range(i, j+1):
    array[num-1] = str(k)
print(" ".join(array))