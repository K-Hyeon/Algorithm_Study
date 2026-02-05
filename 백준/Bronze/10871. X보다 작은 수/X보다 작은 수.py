N, X = map(int, input().split())
array = list(map(int, input().split()))

answer = []
for i in array:
  if i < X: answer.append(str(i))

print(" ".join(answer))