import sys
A, B, V = map(int, sys.stdin.readline().split())

day = 0
while True: 
    day += 1 #하루 경과
    V -= A
    if V == 0: #정상에 올라간순간 빠져나옴
        break 
    V += B
    
print(day)
    