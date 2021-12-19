# from collections import Counter

# word = input().upper()
# result = Counter(word).most_common(2)

# if result[0][1] == result[1][1]:
#     print("?")
# else:
#     print(result[0][0])

#효율성해결
word = input().upper()
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
best = [-1, '']
second = [-2, '']
for k, i in dic.items():
    if i >= best[0]:
        second = best
        best = [i, k]
if best[0] == second[0]:
    print('?')
else:
    print(best[1])