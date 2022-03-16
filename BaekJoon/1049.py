#돈 적게 쓰는 게 핵심
N, M = map(int, input().split())

answer = 0
price_list = []

for _ in range(M):
    #패키지 가격, 낱개 가격
    price = tuple(map(int, input().split()))
    price_list.append(price)

#6개 패키지 묶음과 낱개 가격이 가장 싼 순서대로 정렬
pkg_list = sorted(price_list, key=lambda x : x[0])
one_list = sorted(price_list, key=lambda x : x[1])

if pkg_list[0][0] <= one_list[0][1] * 6: #패키지가 낱개*6보다 싸면
    #묶음으로 여러개 사고 남은 만큼 낱개로 구매
    answer = pkg_list[0][0] * (N // 6) + one_list[0][1] * (N % 6)
    # 이 때, 남은 만큼 낱개로 구매하는 가격보다 묶음으로 사고 남기는 게 더 싸면
    if pkg_list[0][0] < one_list[0][1] * (N % 6):
        answer = pkg_list[0][0] * (N//6 + 1) #패키지 묶음 +1 사기
else: #패키지 묶음보다 낱개 *6 가격이 더 싸면 
    answer = one_list[0][1] * N #모두 낱개 가격으로 구매

print(answer)