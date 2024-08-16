class Solution {
    fun solution(a: Int, d: Int, included: BooleanArray): Int {
        var answer: Int = 0
        
        for(i in 0..included.size - 1){
            if(included[i]) answer += a + (d * i)
        }
        
        return answer
    }
}
