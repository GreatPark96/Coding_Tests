def solution(x):
    listNum = list(str(x))
    sumNum = sum(list(map(int,listNum)))
    if x % sumNum == 0:
        return True
    else:
        return False