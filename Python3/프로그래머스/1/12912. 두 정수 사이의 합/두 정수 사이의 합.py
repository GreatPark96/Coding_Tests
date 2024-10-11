def solution(a, b):
    num = []
    first = a
    second = b

    if b < a:
        first = b
        second = a        
    for i in range(first, second + 1):
        num.append(i)
    return sum(num)