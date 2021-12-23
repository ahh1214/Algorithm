test_case = int(input())

for i in range(test_case):
    str = input().split()
    strn = int(str[0])
    string = str[1]
    
    for j in string:
        print(j*strn, end='')
    print()