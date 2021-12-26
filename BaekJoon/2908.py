num = input().split()

a = int(num[0][-1::-1])
b = int(num[1][-1::-1])

if a > b:
    print(a)
else:
    print(b)