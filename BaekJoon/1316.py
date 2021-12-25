wd_len = int(input())

wd_cnt = wd_len
for i in range(wd_len):
    wd = input()
    for j in range(len(wd)-1):
        if wd[j]==wd[j+1]: #알파벳이 연속해서 나오는 경우
            pass
        elif wd[j] in wd[j+1:]: #연속하지않는데 뒤에 존재
            wd_cnt -=1
        
print(wd_cnt)