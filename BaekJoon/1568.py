N = int(input())
result = 0
K=1

while N > 0: #N이 0보다 클 때
    if N < K: #K보다 N이 작으면
        K = 1 #K를 다시 1로 초기화
    N -= K #부르는 자연수만큼 빼줌
    K += 1 #하나씩 증가
    result+=1 #초 증가

print(result)