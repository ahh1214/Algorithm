import math
#먼저 배포돼야 하는 순서대로 진도가 적힌 배열, 작업 개발 속도가 적힌 배열 
def solution(progresses, speeds):
    result = []
    answer = []
    for p, s in zip(progresses, speeds):
        complete_day = math.ceil((100-p)/s)
        result.append(complete_day)
    
    cnt=1
    reset=result[0]
    for i in range(1,len(result)):
        if reset >= result[i]:
            cnt+=1
        else:
            reset=result[i]
            answer.append(cnt)
            cnt=1    
    answer.append(cnt)
        
    return answer #각 배포마다 몇 개의 기능이 배포되는지

a_case = solution([93, 30, 55],	[1, 30, 5])
b_case = solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])