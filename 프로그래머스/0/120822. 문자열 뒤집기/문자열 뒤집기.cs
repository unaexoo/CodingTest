using System;

public class Solution {
    public string solution(string my_string) {
 string answer = "";
        char[] strArr = my_string.ToCharArray();
        Array.Reverse(strArr);
        answer = string.Concat(strArr);
        return answer;
    }
}