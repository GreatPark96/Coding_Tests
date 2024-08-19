class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        for(query in queries){
            for(i in query[0]..query[1]){
                if((i % query[2] == 0)) arr[i]++
            }
        }
        return arr
    }
}