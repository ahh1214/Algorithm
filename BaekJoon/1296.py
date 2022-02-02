yd_name = input() #연두의 영어이름
n = int(input())
team_names = [input() for _ in range(n)] #팀명 리스트

max_score = 0
result = 'Z' * 20 #임의로 문자열 저장 (20보다 작다는 조건)
for name in team_names:
    # 각 L,O,V,E 개수 세기
    L = yd_name.count('L') + name.count('L')
    O = yd_name.count('O') + name.count('O')
    V = yd_name.count('V') + name.count('V')
    E = yd_name.count('E') + name.count('E')
    score = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    
    if score > max_score:
        max_score = score
        result = name
    elif score == max_score: #확률 높은 팀이름이 여러개면 사전 순 정렬
        max_score = score
        result = min(result, name) #사전 앞 순서인 팀명 저장
print(result)