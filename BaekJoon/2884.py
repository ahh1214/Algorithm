h, m = map(int, input().split())

if m < 45: #분이 45보다 작으면
    if h == 0:
        h = 23
        m = 60 - (45 -m)
    else:
        h -=1 #시간은 한시간 줄이고
        m = 60 - (45-m) #45에서 미리 0이되게끔 분을 빼고 60에서 뺌
else:
    m = m - 45
    
print(h, m)