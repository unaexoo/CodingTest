using System;
using System.Linq;
public class Solution {
    public string solution(string my_string) {
 var str=my_string.Select(s => char.IsUpper(s) ? char.ToLower(s) : char.ToUpper(s));
        string answer = new String(str.ToArray());
        return answer;
    }
}