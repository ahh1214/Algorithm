from itertools import combinations

def solution(number, k):
    result=[]

    num_len = len(number) - k
    result.append(list(map(''.join, combinations(number, num_len))))
    
    return max(result[0])