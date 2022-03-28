import sys

input = sys.stdin.readline

n = int(input())

cnt = 0 #꼽을 수 있는 수 카운팅

for i in range(n):
    cnt += int(input())
    
print(cnt - ( n-1 ))