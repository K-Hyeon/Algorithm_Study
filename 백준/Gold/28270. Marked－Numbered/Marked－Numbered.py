C = int(input())
M = list(map(int, input().split()))

if M[0] != 1:
    print(-1)
    exit(0)

visit = [0] * (C + 1)
res = []
benum = 0
for num in M:
    if num > C:
        print(-1)
        exit(0)
        
    if num < benum:
        visit[num] += 1
        res.append(str(visit[num]))
        
    else:
        if num > benum: visit[num] = 0
        visit[num] += 1
        res.append(str(visit[num]))
    benum = num
print(" ".join(res))