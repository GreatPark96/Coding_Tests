class Solution {
    fun solution(num_list: IntArray): Int {
        var even: Int = num_list.filterIndexed{ index, value -> index % 2 != 0 }.sum()
        var odd: Int = num_list.filterIndexed{ index, value -> index % 2 == 0 }.sum()
        
        return if(even < odd) odd else even
    }
}