class Solution {
    fun solution(my_string: String, is_suffix: String): Int {
        var answer: Array<String> = arrayOf<String>()
        
        for(i in 0..my_string.length - 1){
            answer += my_string.substring(i..my_string.length - 1) 
        }
        return if(answer.contains(is_suffix)) 1 else 0
    }
}