class Solution {
    fun solution(my_string: String): IntArray {
        var answer: IntArray = intArrayOf()
        for(i in 1..52) answer += 0
        
        for(chr in my_string){
            var idx: Int = if(chr.toInt() in 65..90) chr.toInt() - 65  
                else chr.toInt() - 97 + 26
            answer[idx]++
        }
        return answer
    }
}