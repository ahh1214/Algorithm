def solution(citations): 
    citations.sort(reverse=True)
    for i in range(len(citations)): #01234
        a = [i+1 <= item for item in citations] #원소별로 T/F로 비교
        if i+1 == a.count(True) and i+1 >= a.count(False):
            return i+1
    return 0