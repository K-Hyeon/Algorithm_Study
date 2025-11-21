from collections import deque

n, w, L = map(int, input().split(' '))
trucks = list(map(int, input().split()))
trucks.reverse()

que = deque()

weight = 0
time = 0

while True:
    if len(trucks) == 0 and weight == 0:
        break
    if len(que) == w:
        remove = que.popleft()
        weight -= remove
    if len(trucks) > 0 and (weight + trucks[-1]) <= L :
        truck = trucks.pop()
        que.append(truck)
        weight += truck
    else:
        que.append(0)        
    time += 1

print(time)