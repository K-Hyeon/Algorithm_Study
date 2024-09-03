import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, T = map(int, input().split())
    graph[s].append((e, T))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))

    dis = [1e9] * (N+1)
    dis[start] = 0
    while que:
        value, point = heapq.heappop(que)
        if dis[point] < value: continue

        for node_idx, node_cost in graph[point]:
            cost = value + node_cost
            if dis[node_idx] > cost:
                dis[node_idx] = cost
                heapq.heappush(que, (cost, node_idx))
    return dis
    

result = 0
for start in range(1, N+1):
    if start == X or start > N: continue
    first = dijkstra(start)
    second = dijkstra(X)
    result = max(result, first[X] + second[start])
print(result)