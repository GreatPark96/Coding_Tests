class Solution {
    fun solution(myString: String, pat: String): Int {
        val result = myString.map{if(it == 'A') 'B' else if(it == 'B') 'A' else it}.joinToString("").indexOf(pat)      
        return if(result == -1) 0 else 1
    }
}