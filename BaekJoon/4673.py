#10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력
num = set(range(1, 10001))
tmp_num = set() #생성자가 존재하는 수 저장

for i in range(1, 10001): #1 ~10000
    for j in str(i):
        i += int(j)
    tmp_num.add(i) #생성자가 존재하는 수 리스트에 추가
    
self_num = num - tmp_num
self_num = sorted(self_num)

for i in self_num:
    print(i)