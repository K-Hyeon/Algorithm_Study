N = int(input())

def backtracking(idx):
    for i in range(1, (idx//2) + 1):
        if s[-i:] == s[-2*i:-i]: return -1

    if idx == N:
        print("".join(s))
        return 0

    for i in range(1, 4):
        s.append(str(i))
        if backtracking(idx + 1) == 0:
            return 0
        s.pop()

s = []
backtracking(0)