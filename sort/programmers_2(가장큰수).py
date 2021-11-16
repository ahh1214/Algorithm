def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))

    
# from itertools import permutations

# def solution(numbers):
#     result = list( permutations(numbers, len(numbers)))
#     max_num = 0
#     for content in result:
#         content = list(content)
#         check = "".join(map(str,content))
#         # print(check)
#         check = int(check)
#         if max_num < check:
#             max_num = check
#     answer = str(max_num)
#     return answer