class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        for(query in queries){
            for(i in query[0]..query[1]) arr[i]++
        }
        return arr
    }
}