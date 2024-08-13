class Solution {
    fun solution(arr: Array<String>): String {
        var answer: String = ""
        
        for(chr in arr){
            answer = answer + chr
        }
        return answer
    }
}