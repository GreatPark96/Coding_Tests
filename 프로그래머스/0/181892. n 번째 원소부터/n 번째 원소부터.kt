class Solution {
    fun solution(num_list: IntArray, n: Int): ArrayList<Int> {
        val answer: ArrayList<Int> = arrayListOf()
        for(i in (n - 1)..num_list.size - 1) answer.add(num_list[i])
        return answer
    }
}