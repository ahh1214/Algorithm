
number = []
for i in range(9):   
    number.append(int(input()))

max_num = max(number)

print(max_num)
print(number.index(max_num)+1)