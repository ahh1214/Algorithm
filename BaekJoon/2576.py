total = 0
n = []
for i in range(7):
    num = int(input())
    if num % 2 != 0:
       n.append(num)

if n: #n에 값이 존재할 때
    print(sum(n))
    print(min(n)) 
else: #값이 존재하지 않을 때 
    print(-1)
        
