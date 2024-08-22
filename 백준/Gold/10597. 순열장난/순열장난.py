arr = input().strip()

N = 0
len_arr = len(arr)
if len_arr > 9: N = 9 + (len_arr - 9) // 2
else: N = len_arr
num_list = [i for i in range(1, N + 1)]

one = True
answer = []
def space(start, end):
    global one, answer
    if end > len(arr):
        if one: print(" ".join(answer))
        one = False
        return answer
    num1 = int(arr[start:end])
    num2 = int(arr[start:end+1])
        
    if num1 in num_list:
        answer.append(arr[start:end])
        num_list.remove(num1)
        space(start+1, end+1)
        answer.remove(arr[start:end])
        num_list.append(num1)
    if num2 in num_list:
        answer.append(arr[start:end+1])
        num_list.remove(num2)
        space(start+2, end+2)
        answer.remove(arr[start:end+1])
        num_list.append(num2)
space(0, 1)