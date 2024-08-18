class Solution {
    fun solution(a: Int, b: Int, c: Int): Int {

        return when{ 
            (a != b) && (a != c) && (b != c) -> {
                a + b + c
            }
            (a == b) && (a == c) && (b == c)  -> {
                (a + b + c) * ((a * a) + (b * b) + (c * c)) * ((a * a * a) + (b * b * b) + (c * c * c)) 
            }
             (a == b) || (a == c) || (b == c) -> {
                (a + b + c) * ((a * a) + (b * b) + (c * c))
            }
            else -> {0}
        }
    }
}