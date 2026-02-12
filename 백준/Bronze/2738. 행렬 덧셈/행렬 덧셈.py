N, M = map(int, input().split())

arr1 = []
arr2 = []
for i in range(2):
  for j in range(N):
    if i == 0: arr1.append(list(map(int, input().split())))
    else: arr2.append(list(map(int, input().split())))
    
answer = [[0]*M for i in range(N)]
for i in range(N):
  for j in range(M):
    answer[i][j] = str(arr1[i][j] + arr2[i][j])
for i in range(N):
  print(" ".join(answer[i]))