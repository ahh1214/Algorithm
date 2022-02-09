n = int(input()) #진짜 약수의 개수
a = list(map(int, input().split())) #진짜 약수

a_max = max(a) #약수들 중에 가장 큰 값
a_min = min(a) #약수들 중에 가장 작은 값
print(a_max * a_min) #두 값을 곱하면 실제 N이 나옴