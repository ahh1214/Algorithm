n, m = map(int,input().split()) #성의 세로x가로 크기 
board = []

for _ in range(n):
    board.append(input()) #성의 상태 

a, b = 0, 0

for i in range(n):
    if "X" not in board[i]: #경비원이 없으면
        a += 1

for j in range(m):
    if "X" not in [board[i][j] for i in range(n)]:
        b += 1

print(max(a ,b))
