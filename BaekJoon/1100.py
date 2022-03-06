board = []
# 체스판 받아옴
for i in range(8) :
    board.append(list(map(str, input())))

#흰색 위에 말 개수
cnt = 0
# 8x8 크기의 체스판
for i in range(8) :
    for j in range(8) :
        # 체스판의 좌표를 더했을 때, 짝수이면 흰색 칸
        if (i+j) % 2 ==0 :
            # 흰색 칸인데 그 위에 말(F)이 존재하면
            if board[i][j]=='F':
                cnt += 1 # +1

print(cnt)
