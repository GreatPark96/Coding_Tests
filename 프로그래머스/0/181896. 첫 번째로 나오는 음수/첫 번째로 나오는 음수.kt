class Solution {
    fun solution(num_list: IntArray): Int {
        //return num_list.withIndex().firstOrNull {it.value < 0}?.index ?: -1
        return num_list.indexOfFirst { it < 0 }
    }     
}