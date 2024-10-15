def solution(n):
    answer = []
    
    while n >= 3:
        answer.append(str(n % 3)) 
        n = n//3
    answer.append(str(n))
    
    answer = "".join(answer)
    return int(answer,3)
    