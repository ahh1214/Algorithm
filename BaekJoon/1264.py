wd = ['a','e','i','o','u']

while 1:    
    eng = input().lower()
    if eng == '#': break
    
    cnt =0 
    for i in eng:
        if i in wd:
            cnt +=1

    print(cnt)

