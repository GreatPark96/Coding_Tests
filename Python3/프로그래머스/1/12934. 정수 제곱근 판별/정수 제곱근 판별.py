def solution(n):
    result = n**(1/2)
    print(type(result))
    if result.is_integer():
        return pow((result + 1), 2)
    else:
        return -1
