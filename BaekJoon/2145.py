while(True):
    n = int(input()) #매번 숫자 입력받기
    
    if n == 0: #마지막 입력은 break
        break
    while(n > 9): #n이 한자리수가 아닐 경우에 한자리가 될떄까지 계속 반복 
        n_list = list(str(n))
        n = sum(map(int, n_list)) #각 자릿수 다 더하기
        
    print(n)