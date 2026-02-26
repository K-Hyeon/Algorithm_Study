Test_case = int(input())
for _ in range(Test_case):
  num = int(input()) # 센트 단위
  
  Quarter = num // 25
  num %= 25
  Dime = num // 10
  num %= 10
  Nickel = num // 5
  num %= 5
  Penny = num // 1
  print(f'{Quarter} {Dime} {Nickel} {Penny}')