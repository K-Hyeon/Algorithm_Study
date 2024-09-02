from collections import deque

N, K = map(int, input().split())
arr = deque()
for i in range(1, N+1):
    arr.append(i)

answer = []
while arr:
    for i in range(K-1):
        arr.append(arr.popleft())
    answer.append(str(arr.popleft()))
print("<", end='')
print(", ".join(answer), end='')
print(">", end='')