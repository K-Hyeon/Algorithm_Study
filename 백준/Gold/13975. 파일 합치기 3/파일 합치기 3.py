import heapq

T =  int(input())
for _ in range(T):
    sum = 0
    K =  int(input())
    arr =  list(map(int, input().split()))
    heapq.heapify(arr)
    
    while len(arr) > 1:
        a, b = heapq.heappop(arr), heapq.heappop(arr)
        ab = a + b
        sum += ab
        heapq.heappush(arr, ab)

    print(sum)