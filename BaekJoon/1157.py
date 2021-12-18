from collections import Counter

word = input().upper()
result = Counter(word).most_common(2)

if result[0][1] == result[1][1]:
    print("?")
else:
    print(result[0][0])