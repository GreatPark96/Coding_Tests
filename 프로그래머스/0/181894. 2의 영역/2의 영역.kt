class Solution {
    fun solution(arr: IntArray): IntArray {
        return if(! arr.contains(2)) intArrayOf( -1)
        else arr.sliceArray(arr.indexOf(2)..arr.lastIndexOf(2))
    }
}