class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = {};
        int cnt = 0;
        int idx = 0;
        
        for(int i = start_num; i >= end_num; i--) cnt++;
        answer = new int[cnt];
        
        for(int i = start_num; i >= end_num; i--){
            answer[idx] = i;
            idx++;
        }
        
        return answer;
    }
}