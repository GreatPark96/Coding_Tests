def solution(s):
    answer = []
    modZero = 0
    cnt = 0
    
    while(s != "1"):
        s = list(s)
        for i in range(0, len(s)):
            if s[i] == "0":
                s[i] = ""
                modZero += 1
        s = "".join(s)
        s = len(s)
        s = bin(s)[2:]
        cnt += 1
    return [cnt, modZero]