answer = set()

for i in range(10):
  a = int(input())
  answer.add(a % 42)

print(len(answer))