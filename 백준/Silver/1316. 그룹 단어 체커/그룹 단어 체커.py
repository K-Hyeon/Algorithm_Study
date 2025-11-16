N = int(input())

answer = 0
for _ in range(N):
    lst = []
    valid = True
    text = input()
    for i in range(len(text)):
        if text[i] not in lst:
            lst.append(text[i])
        elif text[i] != text[i - 1]:
            valid = False
    if valid == True : answer += 1
print(answer) 