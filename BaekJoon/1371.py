import sys

str_eng = sys.stdin.read()
li = [0]*26 #알파벳개수만큼 자리할당

for ch_eng in str_eng:
    if ch_eng.islower(): #소문자로 변경
        li[ord(ch_eng)-97] += 1 #아스키코드
        
for i in range(26):
    if li[i] == max(li): 
        print(chr(97+i), end='') #가장 많이 쓰인 알파벳 출력