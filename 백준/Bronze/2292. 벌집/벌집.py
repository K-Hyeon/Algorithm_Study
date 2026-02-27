N = int(input())

if N == 1: print(1)
else:
  answer = 1
  num = 1
  while 1:
    answer += (6 * num)
    num += 1
    if answer >= N:
      print(num)
      break