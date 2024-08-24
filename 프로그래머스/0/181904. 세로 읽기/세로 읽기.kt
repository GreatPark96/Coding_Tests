class Solution {
    fun solution(my_string: String, m: Int, c: Int): String {
        var answer: String = ""
        var idx: Int = c - 1
        while(idx < my_string.length){
            answer = answer + my_string[idx]
            idx += m
        }
        return answer
    }
}