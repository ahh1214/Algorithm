a = input()
b = input()
c = input()

values = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
             'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
             'grey': 8, 'white': 9}
 
 # 10의 (값)제곱 
print((values[a] * 10 + values[b]) * (10 ** values[c]))
