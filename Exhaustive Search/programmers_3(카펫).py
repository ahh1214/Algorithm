from itertools import combinations, product

def solution(brown, yellow):
    answer = []
    divisorsList = [] #약수 구함

    for i in range(1, yellow + 1):
        if (yellow % i == 0) :
            divisorsList.append([i, yellow//i]) 
    
    for j in divisorsList:
        total = (int(j[0])+2) * (int(j[1])+2)
    
        if total == int(brown + yellow):
            if int(j[0]) >= int(j[1]):
                   answer.append([int(j[0])+2,int(j[1])+2])
            
    return answer[0]
