def solution(s):
    splitData = s.split(" ")
    intData = list(map(int, splitData))
    return str(min(intData)) + " " + str(max(intData)) 
    