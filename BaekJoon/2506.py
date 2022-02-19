import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
bonus,result = 1,0
for i in a:
    if i:
        result+=bonus
        bonus+=1
    else:
        bonus=1
print(result)