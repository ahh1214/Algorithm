from collections import deque
#문서 중요도가 담긴 배열(1~9), 요청 문서 대기 목록(0~99)
def solution(priorities, location):
    cnt=0
    deq = deque(priorities)
    result = deque()
    [result.append([i, prior]) for i, prior in enumerate(deq)]
    
    while True:
        check = result.popleft() #체크할 문서
        if any([check[1] < item[1] for item in result]): #뒤 요소들 중에 자기보다 큰 값이 하나라도 있으면
            result.append(check) #뒤로 넘김
        else: #자기 차례이면
            cnt+=1 #그대로 나가면서 +1
            if location == check[0]: #올바른 차례 때, location과 같은 문서라면
                return cnt #몇 번째로 인쇄되는지 반환 후 break
                break

a_case = solution([2,1,3,2],2) #1
b_case = solution([1,1,9,1,1,1],0) #5