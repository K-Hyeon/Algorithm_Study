N = int(input())
S = input().strip()

# 유사 ANA 문자열의 개수를 세기 위한 변수
count = 0

# 모든 길이 3 이상인 부분 문자열을 검사
for start in range(N):
    for end in range(start + 3, N + 1):
        # 부분 문자열 추출
        substring = S[start:end]
        
        # 조건 체크
        if substring[0] == 'A' and substring[-1] == 'A' and \
           substring.count('A') == 2 and substring.count('N') == 1:
            count += 1

# 결과 출력
print(count)