H, M = map(int, input().split())
time = int(input())

if M + time < 60 : print("{} {}".format(H, M+time))
else : print("{} {}".format((H + (M+time)//60)%24, (M+time)%60))