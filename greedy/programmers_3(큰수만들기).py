from itertools import combinations

def solution(number, k):
    result=[]

    num_len = len(number) - k
    result.append(list(map(''.join, combinations(number, num_len))))
    
    return max(result[0])

a_case = solution("1924",2) #94
b_case = solution("1231234", 3) #3234
c_case = solution("4177252841", 4) #775841

print(a_case)
print(b_case)
print(c_case)