def solution(nums):
    chs = len(nums) / 2 
    cata = len(list(set(nums)))
    return chs if chs < cata else cata 
  

