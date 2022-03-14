N, newScore, P = map(int, input().split())

if N == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    
    if N == P and score[-1] >= newScore:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if score[i] <= newScore:
                result = i + 1
                break
            
        print(result)