class Solution {
    fun solution(myString: String, pat: String): String {
        var index: Int = 0
        
        do{
            if(myString.indexOf(pat, index + 1) != -1) index++ 
            else break
        }while(index != -1)
        
        return myString.substring(0..index + pat.length - 1)
    }
}