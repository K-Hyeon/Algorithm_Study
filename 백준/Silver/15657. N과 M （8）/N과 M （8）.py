import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

num = 0
comb = itertools.combinations_with_replacement(arr, M)
for i in comb:
    for j in i:
        print(j, end=' ')
    print()