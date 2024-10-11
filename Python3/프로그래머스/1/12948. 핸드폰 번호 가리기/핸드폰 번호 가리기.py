def solution(phone_number):
    numberLen = len(phone_number)
    answer = ''
    
    for i in range(0, numberLen - 4):
        answer = answer + "*"

    return answer + phone_number[numberLen - 4:numberLen]

    