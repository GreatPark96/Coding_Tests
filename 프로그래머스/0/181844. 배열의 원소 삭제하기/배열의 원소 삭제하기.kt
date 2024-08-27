class Solution {
    fun solution(arr: IntArray, delete_list: IntArray): IntArray {
        var result: MutableList<Int> = arr.copyOf().toMutableList()
        for(delete in delete_list) result.remove(delete)
        return result.toIntArray()
    }
}