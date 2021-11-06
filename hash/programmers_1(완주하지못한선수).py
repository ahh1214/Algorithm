from collections import Counter

def solution(participant, completion): #선수들 이름 , 완주한 선수들 이름
    
    dict1=Counter(participant)
    dict2=Counter(completion)
    
    result = list(dict1-dict2)

    answer = result[0]
    
    return answer #완주 못한 선수