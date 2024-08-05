import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = A + B
c.sort()

answer = ' '.join(map(str, c))
print(answer)