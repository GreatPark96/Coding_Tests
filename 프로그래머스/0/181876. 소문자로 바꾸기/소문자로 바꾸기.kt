const val MYSTRING_MIN = 1
const val MYSTRING_MAX = 100000

class Solution {
    fun solution(myString: String): String {
        
        return if(myString.length in MYSTRING_MIN..MYSTRING_MAX){
            myString.toLowerCase()
        }else{
            ""
        }
    }
}