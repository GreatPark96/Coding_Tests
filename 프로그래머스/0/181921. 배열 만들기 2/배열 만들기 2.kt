class Solution {
    fun solution(l: Int, r: Int): IntArray {
        var answer: IntArray = intArrayOf()

        for(i in l..r){
            if(i.toString().all{it == '5' || it == '0'}) answer+= i
        }
        
        if(answer.isEmpty()) answer += -1
        return answer
    }
}