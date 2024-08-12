import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

min_sub = 1e9 * 2
left, right = 0, 1
while right < N:
    sub = array[right] - array[left]
    if sub < M:
        right += 1
    elif sub > M:
        min_sub = min(min_sub, sub)
        left += 1
    else:
        min_sub = M
        break
print(min_sub)
