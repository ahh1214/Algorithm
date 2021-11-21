def solution(answers):
    answer = []
    result = []
    p1_cnt = 0
    p2_cnt = 0
    p3_cnt = 0
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        
        if answers[i] == p1[i%5] :
            p1_cnt +=1 
            # print(p1_cnt)
        if answers[i] == p2[i%8] :
            p2_cnt +=1 
        if answers[i] == p3[i%10] :
            p3_cnt +=1 
            
    result=[p1_cnt,p2_cnt,p3_cnt]
    
    max_score = max(result)
    for j in range(len(result)):
        if result[j] ==  max_score:
            answer.append(j+1)
    
    return answer

a_case = solution([1,2,3,4,5]) #1
b_case = solution([1,3,2,4,2]) #1,2,3
