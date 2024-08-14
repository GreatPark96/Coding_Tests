class Solution {
    fun solution(num_list: IntArray): Int {
        var multi: Int = 1
        var sum: Int = 0
        
        for(num in num_list){
            multi *= num
            sum += num
        }
        return when{
            multi < (sum * sum) -> {
                1
            }
            else -> {
                0
            }
        }
    }
}