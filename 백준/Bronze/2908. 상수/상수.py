arr = list(map(str, input().split()))
num = ['', '']

for i in range(2):
  for j in range(len(arr[i])):
    num[i] += arr[i][len(arr[i])-j-1]
if int(num[0]) > int(num[1]): print(int(num[0]))
else: print(int(num[1]))