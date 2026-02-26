num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

N, B = map(int, input().split())
while N != 0:
    answer = num_list[N % B] + answer
    N //= B

print(answer)