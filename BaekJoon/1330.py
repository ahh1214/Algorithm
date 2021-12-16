question = input().split() #공백으로 구분

a = int(question[0])
b = int(question[1])

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")


