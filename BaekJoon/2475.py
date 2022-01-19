num = list(map(int,input().split()))

total = 0
for i in num:
    total += i*i 
    k_num = total%10

print(k_num)
