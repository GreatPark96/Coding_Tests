def solution(wallet, bill):
    answer = 0
    wallet = sorted(wallet)
    bill = sorted(bill)
    
    while wallet[0] < bill[0] or wallet[1] < bill[1]:       
        bill[-1] //= 2
        bill = sorted(bill)
        answer += 1
            
    return answer