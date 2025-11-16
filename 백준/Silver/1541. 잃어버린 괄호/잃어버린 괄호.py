board = input().strip()

parts = board.split('-')
first = sum(map(int, parts[0].split('+')))

result = first
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)