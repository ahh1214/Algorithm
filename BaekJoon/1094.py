x = int(input())
cnt = 1
result = []
result.append(64)

while 1:
    if sum(result) == x:
        break
    a = result.pop()
    
    if a // 2 >= x:
        result.append(a//2)
    elif a == 1:
        continue
    else:
        result.append(a//2)
        result.append(a//2)
        
print(len(result))