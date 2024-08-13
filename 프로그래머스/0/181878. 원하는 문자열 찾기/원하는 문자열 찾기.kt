class Solution {
    fun solution(myString: String, pat: String): Int {
        if(myString.toLowerCase().indexOf(pat.toLowerCase()) == -1) return 0
        else return 1
    }
}