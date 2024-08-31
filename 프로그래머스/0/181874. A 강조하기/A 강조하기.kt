class Solution {
    fun solution(myString: String): String  = myString.map{ if(it.toString() == "a") it.toUpperCase() else if(it.toString() != "A" && it.isUpperCase()) it.toLowerCase() else it.toString()}.joinToString("")
}