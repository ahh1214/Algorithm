X = int(input())
cnt = 0

for n in range(1, X+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수(두자릿수)
        cnt += 1 
    
    else :   #자연수가 100이상일때 부터는 
        nums = list(map(int, str(n))) # 자릿수마다 수 분리 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 이면
            cnt+=1 #+1
            
print(cnt)