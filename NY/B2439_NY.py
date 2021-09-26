#백준 - 별 찍기2 2439 

n = int(input("n 입력 : "))
k = n-1
for i in range (1, n+1, 1) :
    print(" " * k + "*" * i)
    k = k - 1

