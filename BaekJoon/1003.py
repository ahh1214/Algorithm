zero = [1,0,1]
one = [0,1,1]

def fibo (num):
    leng = len(zero)
    if num >= leng:
        for i in range(leng,num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))
    
T = int(input())

for _ in range(T):
    fibo(int(input()))