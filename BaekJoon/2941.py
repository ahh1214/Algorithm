input = input()

cro_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro_alpha:
    input = input.replace(i,'*')

print(len(input))