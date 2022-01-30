n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    result = a + b
    print("Case #%s: %s"%(i+1, result ))