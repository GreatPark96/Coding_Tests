fun main(args: Array<String>) {
    val s1 = readLine()!!
    var result: String = ""
    
    for(v in s1){
        val convert = if(v.isUpperCase()){
            result += v.toLowerCase()
        }else{
            result += v.toUpperCase()
        }
    }
    print(result)
}
