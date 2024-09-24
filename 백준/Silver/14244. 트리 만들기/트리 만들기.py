n, m = map(int, input().split())

leaf = 0
if m == 0:
    leaf = 1

last_leaf = 1
for i in range(1, n):
    if m > leaf:
        print(0, i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i