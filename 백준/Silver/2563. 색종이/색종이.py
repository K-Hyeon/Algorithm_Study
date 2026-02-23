x_len = 100
graph = [[0]*x_len for _ in range(x_len)]
for _ in range(int(input())):
  x, y = map(int, input().split()) # 10 X 10
  for i in range(x-1, x+9):
    for j in range(x_len-y-10, x_len-y):
      graph[j][i] = 1


answer = 0
for i in range(x_len):
  answer += sum(graph[i])
print(answer)