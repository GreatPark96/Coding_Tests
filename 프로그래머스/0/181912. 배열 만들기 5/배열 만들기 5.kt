class Solution {
    fun solution(intStrs: Array<String>, k: Int, s: Int, l: Int): IntArray {
        var answer: IntArray = intArrayOf()
        var subInt: Int = 0
        for(intStr in intStrs){
            subInt = intStr.substring(s..l+s-1).toInt()
            if(subInt > k) answer += subInt
        }
        return answer
    }
}