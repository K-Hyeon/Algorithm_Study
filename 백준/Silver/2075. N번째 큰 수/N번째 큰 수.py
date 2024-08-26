import heapq

N = int(input())
max_arr = []

for _ in range(N):
    arr = map(int, input().split())
    for num in arr:
        if len(max_arr) < N:
            heapq.heappush(max_arr, num)
        else:
            if max_arr[0] < num:
                heapq.heappop(max_arr)
                heapq.heappush(max_arr, num)
print(max_arr[0])