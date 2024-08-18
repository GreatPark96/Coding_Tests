class Solution {
    fun solution(code: String): String {
        var ret: String = ""
        var mode: Boolean = false;
        
        for(i in code.indices){
            if(code[i] == '1'){
                mode = !mode
                continue
            }
            
            when(mode){
                true -> {
                   if(i % 2 != 0) ret += code[i] 
                }
                else -> {
                   if(i % 2 == 0) ret += code[i]
                } 
            }   
        }
        if(ret.isEmpty()) return "EMPTY"
        else return ret
    }
}