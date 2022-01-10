num = []

for i in range(10):
    a = int(input())
    b = a % 42
    num.append(b)
    
num = set(num) #중복제거
print(len(num))