class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var tmp: Int = 0;
        
        for(num in num_list){
            tmp = num
            while(tmp != 1){
                answer++;
                if(tmp % 2 == 0) tmp /= 2
                else tmp = (tmp - 1) / 2
            }
        }
        
        return answer
    }
}