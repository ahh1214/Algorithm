star_len = int(input())

for i in range(star_len):
    for j in range(0,i-star_len):
        print("*", end="")
    print()