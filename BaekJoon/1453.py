n = int(input())
seats = [False] * 101
people = list(map(int, input().split()))
result = 0

for person in people:
    if seats[person]:
        result += 1
    else:
        seats[person] = True
print(result)