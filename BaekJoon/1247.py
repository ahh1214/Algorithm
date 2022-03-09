import sys
input=sys.stdin.readline #빠르게 입력 받아오기 위함

for i in range(3) :
    N = int(input())
    num = [int(input()) for _ in range(N)]

    if sum(num) == 0:
        print(0)
    elif sum(num) > 0 :
        print("+")
    else :
        print("-")