def solution(food):
    left = ''
    right = ''
    for i in range(1, len(food)):
        for j in range(0, food[i]//2):
            left += str(i)
    return left + "0" + left[::-1]