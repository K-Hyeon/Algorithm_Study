N = int(input()) # 과목 수
grade = list(map(int, input().split())) # 점수
max_score = max(grade) # 최대 점수

answer = 0
for i in grade:
  answer += i/max_score*100
print(answer/N)