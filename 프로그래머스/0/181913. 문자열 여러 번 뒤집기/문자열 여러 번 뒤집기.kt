class Solution {
    fun solution(my_string: String, queries: Array<IntArray>): String {
        var answer = StringBuilder(my_string)

        for(query in queries){
            var subStr: String =  answer.substring(query[0]..query[1]).reversed()
            answer.deleteRange(query[0], query[1]+1)
            answer.insert(query[0], subStr) 
        }
        
        return answer.toString()
    }
}