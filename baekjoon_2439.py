# BaekJoon_2439

n = int(input())
tmp = 1
for i in range(n):
    for j in range(n-tmp):
        print(" ", end="")
    for k in range(tmp):
        print("*", end="")
    print()
    tmp += 1
