# s : 일부 자리수가 영단어로 치환된 문자열
def solution(s):
    encStr = s
    answer = 0
    numbers = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7","eight" : "8", "nine" : "9", "zero" : "0"}
    
    for key, value in numbers.items():
        encStr = encStr.replace(key, value)
        
    return int(encStr)

    
   
