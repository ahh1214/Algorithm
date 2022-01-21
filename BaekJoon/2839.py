n = int(input())

cnt = 0
while n >= 0:
    if n % 5 == 0: # 설탕이 5의 배수면
        cnt += n//5 #5킬로그램 봉지 최대로 가져가기
        print(cnt) 
        break
    else: #5의 배수가 아니면
        n -= 3 #3킬로그램 한 봉지씩 (5의 배수 될떄까지)
        cnt += 1
else: # while문이 거짓인 경우 (n이 0이 될때까지 5로 안나눠떨어진 경우 ex) n = -2)
    print(-1) 
