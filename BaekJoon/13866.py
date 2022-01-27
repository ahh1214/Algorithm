score = list(map(int, input().split()))

score.sort() #정렬

teamA = score[0] + score[3]
teamB = score[1] + score[2]

result = max(teamA, teamB) - min(teamA, teamB)

print(result)
