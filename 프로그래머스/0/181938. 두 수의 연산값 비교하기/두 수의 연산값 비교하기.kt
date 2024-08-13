class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        val attachStr = a.toString() + b.toString()
        val attachInt = attachStr.toInt()

        if(attachInt >= (2 * a * b)){
            answer = attachInt
        }else if(attachInt < (2 * a * b)){
            answer = (2 * a * b)
        }
        return answer
    }
}