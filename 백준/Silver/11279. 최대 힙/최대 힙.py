import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap: print(0)
        else: print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x))