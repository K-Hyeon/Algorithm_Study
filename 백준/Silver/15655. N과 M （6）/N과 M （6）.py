import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

temp = 0
comb = itertools.combinations(arr, M)
for i in comb:
    if temp == 0: temp += 1
    else: print()
        
    for j in i:
        print(j, end=' ')