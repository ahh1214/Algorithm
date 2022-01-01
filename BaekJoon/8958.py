n = int(input())
for i in range(n):
    score = input()
    score = list(score)
    sum = 0
    cnt = 1
    for i in score:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)