n = int(input())

word_bag = []

for i in range(n):
    word_bag.append(input())
    
word_bag = set(word_bag) #중복제거
word_bag = list(word_bag)


word_bag.sort() #길이가 같은 경우에는 알파벳순으로 정렬 (미리정렬)
word_bag.sort(key = len)

for i in word_bag:
    print(i)