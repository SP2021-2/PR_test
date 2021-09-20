def solution(phone_number):
    answer = ''
    num = len(phone_number)
    answer += "*" * (num - 4)
    answer += phone_number[-4:]
    return answer
