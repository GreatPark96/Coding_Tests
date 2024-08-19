class Solution {
    fun solution(arr: IntArray): IntArray {
        var stk: ArrayList<Int> = ArrayList()
        var i: Int = 0

        while(i < arr.size)
        {
            if(stk.isEmpty()){
                stk.add(arr[i])
            }else if(stk.last() < arr[i]){
                stk.add(arr[i]) 
            }else if(stk.last() >= arr[i]){
                stk.removeLast()
                continue
            }
            i++
        }
        return stk.toIntArray()
    }
}