scale_name = list(map(int, input().split()))

if scale_name == sorted(scale_name):
    print("ascending")
elif scale_name == sorted(scale_name, reverse=True):
    print("descending")
else:
    print("mixed")