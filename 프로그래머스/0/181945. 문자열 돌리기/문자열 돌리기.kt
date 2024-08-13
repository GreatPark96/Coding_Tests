const val MIN_STR_LENGTH = 1
const val MAX_STR_LENGTH = 10

fun main(args: Array<String>) {
    val s1 = readLine()!!
   if(s1.length in MIN_STR_LENGTH .. MAX_STR_LENGTH){
        for(s in s1) println(s)
    }
}