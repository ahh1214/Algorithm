N = int(input())
F_size = list(map(int, input().split()))
C = int(input())

cnt = N
for s in F_size:
    if s > C:
        cnt += (s-1)//C
    elif s == 0:
        cnt -= 1
print(C*cnt)