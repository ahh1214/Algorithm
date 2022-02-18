li=[]
n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)
    cnt += 1

if k > len(li):
    print(0)
else:
    print(li[k-1])