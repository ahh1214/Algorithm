n = input()
init_num = n

cnt = 0
while True:
    if int(n) <= 10:
        n = '0'+n
        
    sum_tmp = 0
    for i in n:
        sum_tmp += int(i)
        
    n = n[-1]+ str(sum_tmp)[-1]
    cnt +=1
    if int(n) == int(init_num):
        break
print(cnt)