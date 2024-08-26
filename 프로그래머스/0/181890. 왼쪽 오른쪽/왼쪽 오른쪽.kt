class Solution {
    fun solution(str_list: Array<String>): Array<String> {
        
        for(i in str_list.indices){
            if(str_list[i] == "l") return str_list.sliceArray(0..i-1)
            else if(str_list[i] == "r") return str_list.sliceArray(i+1..str_list.size-1)
        }
        return arrayOf()
    }
}