X = int(input()) #구매한 총 금액
N = int(input()) # 구매한 물건의 수

answer = 0
for i in range(N):
  a, b = map(int, input().split())
  answer += a*b

if answer == X : print("Yes")
else: print("No")
