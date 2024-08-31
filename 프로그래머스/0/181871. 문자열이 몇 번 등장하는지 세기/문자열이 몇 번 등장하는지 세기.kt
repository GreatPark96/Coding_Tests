class Solution {
    fun solution(myString: String, pat: String): Int {
        var cnt: Int = 0
        var index: Int = 0
        
        do{
            index = myString.indexOf(pat, index)
            if(index != -1){ 
                index++ 
                cnt++ 
            }
        }while(index != -1)
        
        return cnt
    }
}