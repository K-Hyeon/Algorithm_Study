import itertools

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0: break

    comb = itertools.combinations(arr[1:], 6)
    for i in comb:
        for j in i:
            print(j, end=' ')
        print()
    print()