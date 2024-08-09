from collections import defaultdict
 
N = int(input())
arr = list(map(int,input().split()))
 
left, right, set_f = 0, 0, 0
fruit = defaultdict(int)
answer = 0
while right < N:
    if fruit[arr[right]] == 0:
        set_f += 1
    fruit[arr[right]] += 1
 
    while set_f > 2:
        fruit[arr[left]] -= 1
        if fruit[arr[left]] == 0:
            set_f -= 1
        left += 1
 
    answer = max(answer, right - left + 1)
    right += 1

print(answer)