fun main(args: Array<String>) {
    val s1 = readLine()!!
    val result = if(s1.length >= 1 && s1.length <= 1000000){
        "${s1}"
    }else{
        "ERROR"
    }
    print(result)
}