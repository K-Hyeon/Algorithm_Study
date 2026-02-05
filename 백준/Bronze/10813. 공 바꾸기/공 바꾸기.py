N, M = map(int, input().split())
array = [str(i+1) for i in range(N)]

for i in range(M):
  i, j = map(int, input().split())
  temp = array[i-1]
  array[i-1] = array[j-1]
  array[j-1] = temp

print(' '.join(array))