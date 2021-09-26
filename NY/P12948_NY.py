#프로그래머스 - 핸드폰 번호 가리기 12948
def solution(phone_number):
    answer = ''
    num = phone_number
    
    length = len(num)-4
    d = num[length:length+4]
    
    dot = ""
    
    for i in range(length) :
        dot += "*"
        
    answer = dot + d
    
    return answer