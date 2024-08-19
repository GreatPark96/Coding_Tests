class Solution {
    fun solution(n: Int): IntArray {
        var answer: IntArray = intArrayOf(n)
        var num: Int = n
        
        while(num != 1){
            if(num % 2 == 0) num = num / 2
            else num = 3 * num + 1
            answer += num
        }
        
        return answer
    }
}