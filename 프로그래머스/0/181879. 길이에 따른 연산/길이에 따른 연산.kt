class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        val arrSize = num_list.size
        
        if(arrSize >= 11){
            for(num in num_list) answer += num
        }else if(arrSize <= 10){
            answer++
            for(num in num_list) answer *= num
        }
        
        return answer
    }
}