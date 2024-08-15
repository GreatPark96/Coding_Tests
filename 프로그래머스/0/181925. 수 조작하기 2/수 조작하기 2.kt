class Solution {
    fun solution(numLog: IntArray): String {
        var answer: String = ""
        
        for(i in numLog.size - 1 downTo 0){
            if(i == 0) continue
   
            answer += when(numLog[i] - numLog[i - 1]) {
                -1 -> { 's' }
                1 -> { 'w' }
                -10 -> { 'a' }
                10 -> { 'd' }
                else -> { ' ' }
            }
        }
        return answer.reversed()
    }
}