n = input()

for i in range(1, int(n)+1):
    s = ''
    for j in range(int(n)-i):
       s += ' '
    s += '*' * i
    print(s)