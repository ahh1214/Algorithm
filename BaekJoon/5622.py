word = input()
matching = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

time = 0 
for wd in word:
    for alph in matching:      
        if wd in alph: #ex) 'ABC'중 해당 알파벳이 있으면
            time+=matching.index(alph)+3 # 인덱스 값 + 3초
print(time)