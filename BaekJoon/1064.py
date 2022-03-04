# 절댓값이 5000보다 작거나 같은 정수
ax, ay, bx, by, cx, cy = map(int, input().split())

if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)):
    print(-1.0)
    exit(0)

ab_len = ((ax-bx)**2 + (ay-by)**2)**0.5
ac_len = ((ax-cx)**2 + (ay-cy)**2)**0.5
bc_len = ((bx-cx)**2 + (by-cy)**2)**0.5

lens = [ab_len+ac_len, ab_len+bc_len, ac_len+bc_len]
result = max(lens) - min(lens)

print(2*result)