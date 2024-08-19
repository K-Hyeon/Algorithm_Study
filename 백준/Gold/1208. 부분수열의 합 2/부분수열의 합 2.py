import sys
from itertools import combinations
# input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
    
A, B = arr[:N//2], arr[N//2:]
A_sum, B_sum = [], []
for i in range(len(A)+1):
    for j in combinations(A, i):
        A_sum.append(sum(j))
     
for i in range(len(B)+1):
    for j in combinations(B, i):
        B_sum.append(sum(j))
A_sum.sort()
B_sum.sort(reverse=True)
A_len, B_len = len(A_sum), len(B_sum)
    
res = 0
left, right = 0, 0
while left < A_len and right < B_len:
    lvalue, rvalue = A_sum[left], B_sum[right]
    t_sum = lvalue + rvalue
        
    if t_sum == S:
        tleft, tright = left, right
        while tleft < A_len and A_sum[tleft] == lvalue:
            tleft += 1
        while tright < B_len and B_sum[tright] == rvalue:
            tright += 1
        res += (tleft - left) * (tright - right)
        left, right = tleft, tright
    elif t_sum > S: right += 1
    else: left += 1

if S == 0: print(res - 1)
else: print(res)