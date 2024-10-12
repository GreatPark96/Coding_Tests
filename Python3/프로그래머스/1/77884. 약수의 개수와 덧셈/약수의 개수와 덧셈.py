def solution(left, right):
    answer = []
    
    for i in range(left, right + 1):
        factor = []
        for f in range(1, i + 1):
            if i % f == 0:
                factor.append(f)
        if len(factor) % 2 == 0:
            answer.append(i)
        else:
            answer.append(i * -1)

    return sum(answer)