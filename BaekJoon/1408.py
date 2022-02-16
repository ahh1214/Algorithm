h,m,s = map(int,input().split(':'))
h1, m1, s1 = map(int,input().split(':'))

curtime = h*3600 + m*60 + s
totime = h1*3600 + m1*60 + s1

if h > h1:
    totime += 24*3600
    
time = totime - curtime
a = str(time//3600)
b = str((time%3600)//60)
c = str((time%3600)%60)

if (time//3600)//10 == 0:
    a = "0" + str(time//3600)
    
if ((time%3600)//60)//10 == 0:
    b = "0" + str((time%3600)//60)
    
if ((time%3600)%60) // 10 == 0:
    c = "0" + str((time%3600)%60)
    
print(a+":"+b+":"+c)