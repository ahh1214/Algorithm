#test-case 11 번에서 예외 발생

# def solution(citations): 
#     citations.sort(reverse=True)
#     for i in range(len(citations)): #01234
#         a = [i+1 <= item for item in citations] #원소별로 T/F로 비교
#         if i+1 == a.count(True) and i+1 >= a.count(False):
#             return i+1
#     return 0


def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0