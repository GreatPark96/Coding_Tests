def solution(n):
    for i in range (n + 1, 1000001):
        nBin = bin(n).replace("0b", "")
        iBin = bin(i).replace("0b", "")
        if nBin.count("1") == iBin.count("1"):
            return i