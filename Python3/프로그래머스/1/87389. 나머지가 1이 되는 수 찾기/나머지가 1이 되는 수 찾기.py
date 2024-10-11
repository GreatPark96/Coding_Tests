def solution(n):
    answer = 0
    i = 1
    while(1):
        result = n % i
        if(n % i == 1):
            answer = i
            break
        else:
            i += 1
    return answer