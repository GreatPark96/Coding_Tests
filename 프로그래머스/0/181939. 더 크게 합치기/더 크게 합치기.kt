class Solution {
    fun solution(a: Int, b: Int): Int {
        val attachAB: Int = (a.toString() + b.toString()).toInt()
        val attachBA: Int = (b.toString() + a.toString()).toInt()
        
        return if(attachAB > attachBA){
            attachAB
        }else if(attachAB < attachBA){
            attachBA
        }else{
            attachAB
        }
    }
}