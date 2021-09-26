#프로그래머스 - 행렬의 덧셈 12950

def solution(arr1, arr2):
    answer = []
    
    row = len(arr1)
    col = len(arr1[0])
    
    temp = []
    
    for r in range (0, row, 1) :
        for c in range (0, col, 1) :
            sum = arr1[r][c] + arr2[r][c]
            temp.insert(c, sum)
            
        answer.insert(r, temp.copy())
        temp.clear()
            
    return answer
