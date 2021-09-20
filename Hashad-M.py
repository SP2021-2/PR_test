def solution(x):
    num = x
    answer = True
    sum =0
    while(True):
        sum = sum + (num%10)
        num = (int)(num/10)
        if(num == 0):
            break
    
    if(x % sum != 0):
        answer = False
    return answer

