class Solution {
    fun solution(binomial: String): Int {    
        var regex = "[+\\-*]".toRegex()
        val operand = binomial.split(regex).map{it.trim().toInt()}
        val op = regex.findAll(binomial).map { it.value }.toList()[0]
    
        return when(op){
            "+" -> operand[0] + operand[1]
            "-" -> operand[0] - operand[1]  
            "*" -> operand[0] * operand[1] 
            else -> -1
        }
    }
}