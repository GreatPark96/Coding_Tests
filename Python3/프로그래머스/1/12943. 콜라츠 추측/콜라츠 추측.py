def solution(num):
    if num == 1:
        return 0
    count = 0
    cloneNum = num
    
    for i in range(1, 501):
        count += 1
        if cloneNum % 2 == 0:
            cloneNum /= 2
        else:
            cloneNum = cloneNum * 3 + 1
        if cloneNum == 1:
            break
    if count >= 500:
        return -1
    else:
        return count