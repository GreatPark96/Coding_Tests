class Solution {
    fun solution(num_list: IntArray): Int {
        var even: String = ""
        var odd: String = ""
        
        for(num in num_list){
            when{
                (num % 2) == 0 -> {
                    even = even + num.toString()
                }
                else -> {
                    odd = odd + num.toString()
                }
            }
        }
        return even.toInt() + odd.toInt()
    }
}