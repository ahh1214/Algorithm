def solution(array, commands): #숫자담긴 배열, [i,j,k]
    answer = []
    for start, end, idx in commands:
        answer.append(sorted(array[start-1:end])[idx-1])
        
    return answer


a_case = solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]) #5,6,3