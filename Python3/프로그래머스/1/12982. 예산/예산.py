def solution(d, budget):

    pay = 0
    count = 0
    d.sort()
    
    for request in d:
        if pay + request <= budget:
            pay += request
            count += 1
        else:
            break
    
    return count