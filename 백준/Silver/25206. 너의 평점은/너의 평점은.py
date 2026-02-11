total_gr = 0
total_grade = 0
total_num = 0
for test in range(20):
  name, grade, rank = map(str, input().split())
  if rank == 'A+':
    total_gr += 4.5*float(grade)
  elif rank == 'A0':
    total_gr += 4.0*float(grade)
  elif rank == 'B+':
    total_gr += 3.5*float(grade)
  elif rank == 'B0':
    total_gr += 3.0*float(grade)
  elif rank == 'C+':
    total_gr += 2.5*float(grade)
  elif rank == 'C0':
      total_gr += 2.0*float(grade)
  elif rank == 'D+':
    total_gr += 1.5*float(grade)
  elif rank == 'D0':
    total_gr += 1.0*float(grade)
  elif rank == 'F':
    total_gr += 0.0*float(grade)
  else: continue

  total_grade += float(grade)
  total_num += 1
print(f'{total_gr/total_grade}')
