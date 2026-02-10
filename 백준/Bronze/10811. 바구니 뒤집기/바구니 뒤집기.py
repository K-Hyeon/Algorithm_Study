N, M = map(int, input().split())
array = [str(i) for i in range(1, N+1)]

for i in range(M):
  i, j = map(int, input().split())
  for k in range(0, (j-i)//2 + (j-i)%2):
    temp = array[i+k-1]
    array[i+k-1] = array[j-k-1]
    array[j-k-1] = temp
print(' '.join(array))
