class Solution {
    fun solution(arr: IntArray, idx: Int): Int {
        for(i in idx..arr.size-1){
            if(arr[i] == 1) return i
        }
        return -1
    }
}