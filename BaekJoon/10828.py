import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n) :
    word = sys.stdin.readline().split() 
    cmd = word[0]
    
    if cmd =="push" :
        value = word[1]
        stack.append(value)
    
    elif cmd=="pop" :
        if len(stack)==0 :
            print(-1)
        else :
            print(stack.pop())
    
    elif cmd=="size" :
        print(len(stack))
    
    elif cmd=="empty" :
        if len(stack)==0 :
            print(1)
        else : 
            print(0)
    
    elif cmd=="top" : 
        if len(stack)==0 : 
            print(-1)
        else : 
            print(stack[-1])