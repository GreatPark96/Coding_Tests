def solution(numbers):
    numStr = "".join(list(map(str, numbers)))
    notNum = []
    for i in range(0, 10):
        if numStr.find(str(i)) == -1:
            notNum.append(i)
    return sum(notNum)