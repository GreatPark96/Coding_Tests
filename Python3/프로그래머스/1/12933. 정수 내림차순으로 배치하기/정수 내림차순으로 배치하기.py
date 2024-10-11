def solution(n):
    numList = list(str(n))
    numList.sort(reverse = True)
    return int("".join(numList))
   