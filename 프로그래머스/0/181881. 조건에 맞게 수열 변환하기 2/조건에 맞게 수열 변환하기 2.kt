class Solution {
    fun solution(arr: IntArray): Int {
        var answer: Int = 0
        var before:IntArray = intArrayOf()
        var now: IntArray = arr.copyOf()
        
        while(true){
            before = now.copyOf()
            
            now = now.map{
                if(it >= 50 && it % 2 == 0) it / 2
                else if(it < 50 && it % 2 != 0) it * 2 + 1
                else it
             }.toIntArray()
            
            if(before.contentEquals(now)) break
            else answer++
        } 
        return answer
    }
}