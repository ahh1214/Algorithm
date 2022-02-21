N, L = map(int, input().split())

num = str(L)

res = []
tmp = 1

while True :
    if len(res) == N : break
    sign = 0
    tmp_n = str(tmp)

    for i in range(len(tmp_n)) :
        if tmp_n[i] == num :
            sign = 1
            break

    if sign == 0 :
        res.append(tmp)
    tmp += 1

print(max(res))