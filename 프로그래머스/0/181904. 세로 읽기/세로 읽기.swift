import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    var result = ""
    let myStringArray = Array(my_string)

    for i in stride(from: 0, to: myStringArray.count, by: m){
        result.append(myStringArray[i + c - 1])
    }
    return result
}