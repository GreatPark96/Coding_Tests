class Solution {
    fun solution(my_string: String, indices: IntArray): String {
        var answer: CharArray = my_string.toCharArray()
        
        for(idx in indices){
            answer[idx] = ' '
        }
        return String(answer).replace(" ", "")
    }
}