answer = [i for i in range(1, 31)]

for i in range(28):
  a = int(input())
  answer.remove(a)

print(min(answer))
print(max(answer))