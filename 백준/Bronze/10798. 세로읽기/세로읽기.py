arr = []
max_len = 0
for i in range(5):
  a = input()
  if len(a) > max_len: max_len = len(a)
  arr.append(a)

for i in range(max_len):
  for j in arr:
    try:
      print(j[i], end ='')
    except:
      continue