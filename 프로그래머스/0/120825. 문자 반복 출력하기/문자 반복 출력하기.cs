using System;
using System.Linq;
public class Solution {
    public string solution(string my_string, int n) {
      string answer = "";
        char[] ch = my_string.ToCharArray();

        for (int i = 0; i < my_string.Length; i++)
        {
            answer += String.Concat(Enumerable.Repeat(ch[i], n));
        }
        return answer;
    }
}