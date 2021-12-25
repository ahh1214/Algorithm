wd_len = int(input())

wd_cnt = 0
for i in range(wd_len):
    wd = input()
    for j in range(len(wd)-1):
        print(wd.find(wd[j]))
        print(wd.find(wd[j+1]))
