class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var tmp: Int = 0
        
        for(query in queries){
            tmp = arr[query[0]]
            arr[query[0]] = arr[query[1]]
            arr[query[1]] = tmp
        }
        return arr
    }
}