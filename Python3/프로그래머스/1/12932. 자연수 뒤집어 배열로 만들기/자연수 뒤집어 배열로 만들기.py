def solution(n):
    strNum = str(n)
    listNum = list(map(int, list(strNum)))
    listNum.reverse()
    return listNum
