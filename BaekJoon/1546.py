n = int(input()) # 시험 본 과목 수
score = input().split() #세준이의 진짜 점수
score = list(map(int, score))

max_score = max(score) #최대점수

for i in range(n):
    score[i] = score[i]/max_score*100
    
print(sum(score) / n)
