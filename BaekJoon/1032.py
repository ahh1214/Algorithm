n = int(input())

first_dir = list(str(input()))

for i in range(n-1):
    other_dir = list(str(input()))
    for j in range(len(first_dir)):
        if first_dir[j] != other_dir[j]:
            first_dir[j] = '?'
            
print(''.join(first_dir))