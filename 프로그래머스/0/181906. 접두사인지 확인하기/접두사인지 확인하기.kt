class Solution {
    fun solution(my_string: String, is_prefix: String): Int {
        var perfix: Array<String> = arrayOf()
        
        for(i in my_string.lastIndex downTo 0){
            perfix += my_string.substring(0..i)  
        }
        return if(perfix.contains(is_prefix)) 1 else 0
    }
}