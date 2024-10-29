N, T = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
for a in A:
    num = 0
    while True:
        if (T % (a + num)  == 0): break
        elif (T % (a - num) == 0): break
        else: num += 1
    answer += num
print(answer)