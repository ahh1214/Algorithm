n = input().split()

n = list(map(int,n))

x, y = n[0], n[1]
w, h = n[2], n[3]

#x에서 경계값으로 가는 두 가지 방법
x1 = w - x 
x2 = x - 0

#y에서 경계값으로 가는 두 가지 방법
y1 = h - y
y2 = y - 0

result = []
result.extend([x1,x2,y1,y2])

print(min(result))

