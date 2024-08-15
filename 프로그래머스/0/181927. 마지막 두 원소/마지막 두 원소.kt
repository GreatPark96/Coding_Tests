class Solution {
    fun solution(num_list: IntArray): ArrayList<Int> {
        val result: ArrayList<Int> = ArrayList(num_list.toList())
        val arrIdxSize: Int = result.size - 1
        
        if(result.last() > result[arrIdxSize - 1])
            result.add(num_list.last() - result[arrIdxSize - 1])
        else
            result.add(num_list.last() * 2)
        
        return result
    }
}




