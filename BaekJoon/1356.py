N = list(map(int, input()))
nLen = len(N)

if nLen == 1: #한자리수인 경우에는 유진수 No
    print('NO')
else:
    a = b = 1
    
    for i in range(nLen - 1):
        a = b = 1
        for j in range(i + 1):
            a *= N[j]
        for k in range(i + 1, nLen):
            b *= N[k]

        if a == b: #앞 뒤 곱 결과가 같으면
            break
    
    if a == b:
        print('YES')
    else:
        print('NO')