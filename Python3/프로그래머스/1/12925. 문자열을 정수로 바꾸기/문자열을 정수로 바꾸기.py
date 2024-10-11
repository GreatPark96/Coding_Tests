def solution(s):
    if s[0] != '+' and s[0] != '-':
        return int(s)
    else:
        trans = int(s[1:len(s)])
        if s[0] == '-':
            trans *= -1
        return trans