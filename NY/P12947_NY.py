#프로그래머스 - 하샤드 수 12947

def solution(x) :
    numString = str(x)
    length = len(numString)
    sum = 0
    
    for i in range(length-1, -1, -1) :
        sum = sum + int(numString[i])
    return (x % sum == 0)