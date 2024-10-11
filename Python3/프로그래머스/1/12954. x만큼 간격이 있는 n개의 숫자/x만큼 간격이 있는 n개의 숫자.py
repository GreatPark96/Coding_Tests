def solution(x, n):
    answer = []
    sum = 0
    while(1):
        sum = sum + x
        answer.append(sum)
        if len(answer) >= n:
            break
    return answer