def solution(board, moves):
    bsk = []
    cvtBoard = []
    answer = 0
    
    for i in range(0, len(board)):
        cvtBoard.append([])
    

    for i in range(len(board) - 1, -1, -1):
        for idx, val in enumerate(board[i]):
            if val != 0:
                cvtBoard[idx].append(val)

    for m in moves:
        if not cvtBoard[m - 1]:
            continue
        pull = cvtBoard[m - 1][-1]
        cvtBoard[m - 1].pop()
        
        if not bsk:
            bsk.append(pull)
            continue
        
        if pull == bsk[-1]:
            answer += 2
            bsk.pop()
            continue 
        bsk.append(pull)
    return answer
   
