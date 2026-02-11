word = input()

front = word[:len(word)//2]
rear = word[len(word)//2+len(word)%2:]

if front == rear[::-1] : print(1)
else : print(0)