word = input()
word = word.upper()

answer = {}
max_value = 0
for i in word:
  if i in answer:
    answer[i] += 1
  else: answer[i] = 1
  if answer[i] > max_value:
      max_value = answer[i]


answer_value = 0
answer_word = '?'
for key, value in answer.items():
  if value == max_value:
    answer_value += 1
    answer_word = key
if answer_value > 1: print('?')
else: print(answer_word)
