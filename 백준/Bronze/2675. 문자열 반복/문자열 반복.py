test_case = int(input())
for i in range(test_case):
  R, S = map(str, input().split())
  for j in S:
    print(j*int(R),end='')
  print('')