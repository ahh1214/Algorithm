from collections import Counter

def solution(clothes): #의상들이 담긴 배열
    answer = 1
    
    result = []
    for name, kind in clothes:
        result.append(kind)
        
    result = Counter(result) #	ex) Counter({'headgear': 2, 'eyewear': 1})
    
    for i in result.values():
    	answer *= (i+1) #경우의 수 구함
    
    return answer - 1 #아무것도 안입었을 때는 제외시킴