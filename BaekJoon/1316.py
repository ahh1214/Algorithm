# wd_len = int(input())

# wd_cnt = 0
# for i in range(wd_len):
#     wd = input()
#     for j in range(len(wd)-1):
#         print(wd.find(wd[j]))
#         print(wd.find(wd[j+1]))

wd_len = int(input())

wd_cnt = wd_len
for i in range(wd_len):
    wd = input()
    for j in range(len(wd)-1):
        if wd[j] == wd[j+1]:
            pass
        elif wd[j] in wd[j+1:]:
            wd_cnt -=1
            break
print(wd_cnt)