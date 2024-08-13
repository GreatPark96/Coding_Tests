const val MIN_VALUE_SIZE = 1
const val MAX_VALUE_SIZE = 1000

fun main(args: Array<String>) {
    val a = readLine()!!.toInt()
    
    val result = if(a in MIN_VALUE_SIZE .. MAX_VALUE_SIZE){
         if(a % 2 == 0)"${a} is even" else "${a} is odd"
    }else{
        ""
    }
    print(result)
}