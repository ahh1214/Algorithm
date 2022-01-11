a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
mul_list = list(map(int,str(mul)))

for i in range(0,10):
    cnt = 0
    if i in mul_list: # 값이 존재하는지부터 확인
       cnt = mul_list.count(i) # 개수를 구함

    print(cnt) 