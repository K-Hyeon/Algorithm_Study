import itertools
import sys
input= sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

temp = 0
comb = itertools.permutations(array, M)
for i in comb:
    if temp == 0: temp += 1
    else: print()
    for j in i:
        print(j, end = ' ')