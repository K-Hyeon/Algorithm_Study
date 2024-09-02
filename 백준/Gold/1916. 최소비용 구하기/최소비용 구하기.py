import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())

dis = [1e9] * (N+1)
dis[start] = 0

que = []
heapq.heappush(que, (start, 0))
while que:
    node, cost = heapq.heappop(que)
    if dis[node] < cost:
        if node == end: break
        else: continue

    for point in graph[node]:
        value = cost + point[1]
        if dis[point[0]] > value:
            dis[point[0]] = value
            heapq.heappush(que, (point[0], value))

print(dis[end])