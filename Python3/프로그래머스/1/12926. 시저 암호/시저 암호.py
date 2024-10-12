def solution(s, n):
    answer = ''
    
    chk = {"A": ord("A"), "Z": ord("Z"), "a": ord("a"), "z": ord("z")}
    
    for char in s:
        if char == " ":
            answer += " "
            continue
        
        value = ord(char) + n
        if char.isupper():
            if value > chk['Z']:
                value = (value - chk['Z'] - 1) + chk['A']
                
        elif char.islower():
            if value > chk['z']:
                value = (value - chk['z'] - 1) + chk['a'] 
        
        answer += chr(value)
        
    return answer