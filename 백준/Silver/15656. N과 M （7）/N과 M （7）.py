import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

comb = itertools.product(arr, repeat = M)
for i in comb:
    for j in i:
        print(j, end=" ")
    print()