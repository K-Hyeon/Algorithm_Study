H, M = map(int, input().split())

if M >= 45: print("{} {}".format(H, M-45))
elif H >= 1: print("{} {}".format(H-1, M+60-45))
else: print("{} {}".format(23, M+60-45))