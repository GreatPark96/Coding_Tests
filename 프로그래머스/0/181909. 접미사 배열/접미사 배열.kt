class Solution {
    fun solution(my_string: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for(i in 0..my_string.length - 1){
            answer += my_string.substring(i..my_string.length - 1) 
        }
        answer.sort()
        return answer
    }
}