# programmers_12947

def solution(x):
    answer = True
    n1 = x % 10
    n2 = x % 1000 % 100 // 10
    n3 = x % 1000 // 100
    n4 = x // 1000
    if x % (n1 + n2 + n3 + n4):
        answer = False
    else:
        answer = True
    return answer
