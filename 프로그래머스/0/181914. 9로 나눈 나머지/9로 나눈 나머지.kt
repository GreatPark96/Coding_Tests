class Solution {
    fun solution(number: String): Int {
        var sumNum: Int = 0
        number.map{sumNum += it.toString().toInt()}
        return sumNum % 9
    }
}