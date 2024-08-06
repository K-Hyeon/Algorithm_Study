import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

sum, len = 0, 1e9
left, right = 0, 0
while True:
    if sum >= S:
        len = min(len, right - left)
        sum -= array[left]
        left += 1
    elif right == N:
        break
    else:
        sum += array[right]
        right += 1

if len == 1e9: print(0)
else: print(len)